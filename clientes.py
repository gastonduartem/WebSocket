import socket # Para conectarse con el server

# Dirección IP y PORT al que queremos conectarnos
IP = "127.0.0.1"
PORT = 1234

# Creamos el socket del cliente: IPv4 (AF_INET) + TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al servidor
client_socket.connect((IP, PORT))

print("Conectado al servidor.")

# Enviamos un mensaje simple (hay que codificar el string a bytes)
mensaje = "Hola soy el primer cliente"
client_socket.send(mensaje.encode("utf-8"))

print("Mensaje enviado al servidor")

# Cerramos la conexión
client_socket.close()
print("Conexión cerrada")