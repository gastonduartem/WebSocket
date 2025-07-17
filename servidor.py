import socket # Modulo para trabajar con sockets (enviar/recibir datos por red)

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

# Esperamos a que el cliente se conecte (bloquea el programa hasta que alguien se conecte)
client_socket, client_address = server_socket.accept()
print(f"Conexión recibida de {client_address}")

# Recibimos el mensaje del cliente (hasta 1024 bytes)
mensaje = client_socket.recv(1024).decode("utf-8")

# Mostramos el mensaje en consola
print(f"Mensaje recibido: {mensaje}")

# Cerramos la conexión
client_socket.close()
print("Cliente desconectado")
