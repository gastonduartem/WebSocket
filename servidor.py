import socket # Modulo para trabajar con sockets (enviar/recibir datos por red)
import select # Modulo para monitorear vareios sockets al mismo tiempo sin usar hilos

# IP del servidor
IP = "127.0.0.1"
# Puerto que va a escuchar 
PORT = 1234

# Creamos el socket: usamos IPv4 (AF_INET (queremos usar direcciones IPv4 (por ejemplo 127.0.0.1 o 192.168.0.1)) y TCP (SOCK_STREAM(queremos que los datos lleguen completos y en orden))
server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permitimos reusar el puerto rápidamente si el servidor se reinicia (evita error "Address already in use")
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Enlazamos el socket a la IP y puerto de elección
server_socket.bind((IP, PORT))

# Empezamos a escuchar conexiones (max 5 a la par)
server_socket.listen()

print(f"Servidor corriendo en {IP}: {PORT}. Esperando conexiones...")

# Lista que contiene todos los sockets, empezamos solo con el del cliente
sockets_list = [server_socket]

# Diccionario para asociar cada socket del cliente con su nombre de usuario
usuarios = {} # cliente_socket : "nombre"

# Función para recibir mensajes de un cliente especifico
def recibir_mensaje(cliente_socket):

  try:
    #Intentamos recibir hasta 1024 bytes del cliente
    mensaje = cliente_socket.recv(1024)

    # Si el mensaje esta vacío, el cliente se desconecto
    if not mensaje:
      return False
    
    # Devolvemos el mensaje decodificado como string
    return mensaje.decode("utf-8")
  
  except:

    # Si hay un error al recibir, devolvemos false
    return False

# Bucle principal que mantiene al servidor corriendo siempre

while True:

  # select.select se quedan expectantes hasta que uno de los sockets_clientes tenga algo para leer
  sockets_leibles, _, excepcionales = select.select(sockets_list, [], sockets_list)

  # Recorremos los sockets que tengan actividad de lectura
  for socket_notificado in sockets_leibles:

    # Si el socket que notificó  es el del servidor, significa que hay un nuevo cliente conectándose
    if socket_notificado == server_socket:

      # Aceptamos la nueva conexión
      cliente_socket, cliente_direccion = server_socket.accept()

      # Esperamos el primer mensaje del cliente que deberia ser su nombre
      nombre = recibir_mensaje(cliente_socket)

      # Si no escribe nada, ignoramos
      if nombre is False:
        continue

      # Agregamos este nuevo cliente a la lista de sockets a monitorear
      sockets_list.append(cliente_socket)

      # Guardamos el nombre en el diccionario
      usuarios[cliente_socket] = nombre

      print(f"Nueva conexión de {cliente_direccion}, nombre: {nombre}")

    # Si el socket no es el del servidor, es un cliente queriendo enviar un mensaje
    else:

      # Recibimos el mensaje de ese cliente
      mensaje = recibir_mensaje(socket_notificado)

      # Si no recibimos nada, el cliente cerró la conexión
      if mensaje is False:
        print(f"Cliente {usuarios[socket_notificado]} se desconectó")

        # Eliminamos el cliente de las lista activas
        sockets_list.remove(socket_notificado)
        del usuarios[socket_notificado]
        continue

      # Si recibimos un mensaje, formamos el mensaje con su nombre
      nombre = usuarios[socket_notificado]
      mensaje_completo = f"{nombre}: {mensaje}"

      print(f"{mensaje_completo}")

      # Reenviamos el mensaje a todos los demás clientes (broadcast)
      for cliente in usuarios:
        if cliente != socket_notificado:
          try:
            cliente.send(mensaje_completo.encode("utf-8"))
          except:
            # Si no se puede enviar lo eliminamos de las listas
            cliente.close()
            sockets_list.remove(cliente)
            del usuarios[cliente]

      if len(usuarios) == 0:
        print("No quedan clientes conectados. Cerrando servidor...")
        server_socket.close()
        exit()