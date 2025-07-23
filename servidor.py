import socket  # Módulo para trabajar con sockets (enviar/recibir datos por red)
import select  # Módulo para monitorear varios sockets al mismo tiempo sin usar hilos

# IP del servidor
IP = "127.0.0.1"
# Puerto que va a escuchar 
PORT = 1234

# Creamos el socket: usamos IPv4 (AF_INET: queremos usar direcciones IPv4 como 127.0.0.1) y TCP (SOCK_STREAM: queremos que los datos lleguen completos y en orden)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permitimos reusar el puerto rápidamente si el servidor se reinicia (evita error "Address already in use")
# Cambiamos opciones del socket, Nivel: opciones generales del socket, Queremos reusar la dirección (IP + puerto), 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Enlazamos el socket a la IP y puerto de elección
server_socket.bind((IP, PORT))

# Empezamos a escuchar conexiones (máx. 5 a la par)
server_socket.listen()

print(f"Servidor corriendo en {IP}: {PORT}. Esperando conexiones...")

# Lista que contiene todos los sockets, empezamos solo con el del servidor
sockets_list = [server_socket]

# Diccionario para asociar cada socket de cliente con su nombre de usuario
usuarios = {}  # cliente_socket : "nombre"

# Función para recibir mensajes de un cliente específico
def recibir_mensaje(cliente_socket):
    try:
        # Intentamos recibir hasta 1024 bytes del cliente
        mensaje = cliente_socket.recv(1024)

        # Si el mensaje está vacío, el cliente se desconectó
        if not mensaje:
            return False

        # Devolvemos el mensaje decodificado como string
        return mensaje.decode("utf-8")
    
    except:
        # Si hay un error al recibir, devolvemos False
        return False

# Bucle principal que mantiene al servidor corriendo siempre
while True:
    try:
        # select.select se queda expectante hasta que uno de los sockets tenga algo para leer
        sockets_leibles, _, excepcionales = select.select(sockets_list, [], sockets_list)
        # Exception es la clase base de todos los errores en Python,  guarda el detalle del error en la variable e para poder imprimirlo y analizarlo
    except Exception as e:
        print(f"⚠️ Error en select: {e}")
        continue

    # Recorremos los sockets que tengan actividad de lectura
    for socket_notificado in sockets_leibles:

        # Si el socket que notificó es el del servidor, significa que hay un nuevo cliente conectándose
        if socket_notificado == server_socket:
            try:
                # Aceptamos la nueva conexión
                cliente_socket, cliente_direccion = server_socket.accept()

                # Esperamos el primer mensaje del cliente que debería ser su nombre
                nombre = recibir_mensaje(cliente_socket)

                # Si no escribe nada, ignoramos
                if nombre is False:
                    continue

                # Agregamos este nuevo cliente a la lista de sockets a monitorear
                sockets_list.append(cliente_socket)

                # Guardamos el nombre en el diccionario
                usuarios[cliente_socket] = nombre

                print(f"Nueva conexión de {cliente_direccion}, nombre: {nombre}")
            except:
                print("❌ Error al aceptar nueva conexión.")
                continue

        # Si el socket no es el del servidor, es un cliente enviando un mensaje
        else:
            mensaje = recibir_mensaje(socket_notificado)

            # Si no recibimos nada, el cliente cerró la conexión
            if mensaje is False:
                nombre = usuarios.get(socket_notificado, "Desconocido")
                print(f"Cliente {nombre} se desconectó")

                # Eliminamos el cliente de las listas activas
                if socket_notificado in sockets_list:
                    sockets_list.remove(socket_notificado)
                if socket_notificado in usuarios:
                    del usuarios[socket_notificado]
                continue

            # Si recibimos un mensaje, formamos el mensaje con su nombre
            nombre = usuarios.get(socket_notificado, "Desconocido")
            mensaje_completo = f"{nombre}: {mensaje}"
            print(f"{mensaje_completo}")
  
            # Reenviamos el mensaje a todos los demás clientes (broadcast)
            for cliente in list(usuarios):
                if cliente != socket_notificado:
                    try:
                        cliente.send(mensaje_completo.encode("utf-8"))
                    except:
                        # Si no se puede enviar, lo eliminamos de las listas
                        cliente.close()
                        if cliente in sockets_list:
                            sockets_list.remove(cliente)
                        if cliente in usuarios:
                            del usuarios[cliente]

    # Manejamos los sockets que presentan errores
    for socket_problematico in excepcionales:
        nombre = usuarios.get(socket_problematico, "Desconocido")
        print(f"⚠️ Socket con error: {nombre}")
        if socket_problematico in sockets_list:
            sockets_list.remove(socket_problematico)
        if socket_problematico in usuarios:
            del usuarios[socket_problematico]
        socket_problematico.close()
