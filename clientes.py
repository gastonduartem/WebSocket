import socket   # Para conectarse con el server
import threading  # Para correr múltiples cosas al mismo tiempo (hilos)
import os  # Para cerrar el programa completamente con os._exit

# Dirección IP y puerto del servidor
IP = "127.0.0.1"
PORT = 1234

# Creamos el socket del cliente: IPv4 (AF_INET) + TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Intentamos conectarnos al servidor
try:
    client_socket.connect((IP, PORT))
except:
    print("❌ No se pudo conectar al servidor. ¿Está corriendo?")
    exit()

# Pedimos el nombre del usuario
nombre = input("Escriba su nombre de usuario: ")

# Enviamos el nombre como primer mensaje al servidor
try:
    client_socket.send(nombre.encode("utf-8"))
except:
    print("❌ No se pudo enviar el nombre al servidor.")
    client_socket.close()
    exit()

# Función que se ejecuta en segundo plano para escuchar mensajes del servidor
def recibir_mensajes():
    try:
        while True:
            mensaje = client_socket.recv(1024)
            if not mensaje:
                print("❌ Conexión cerrada por el servidor.")
                break
            print(mensaje.decode("utf-8"))
    except:
        print("⚠️ Error al recibir mensaje (probablemente el servidor cerró).")
    
    os._exit(0)  # Cerramos completamente el cliente (incluso hilo principal)

# Creamos y lanzamos el hilo para escuchar mensajes
hilo_receptor = threading.Thread(target=recibir_mensajes)
hilo_receptor.start()

# Bucle principal para que el usuario pueda enviar mensajes
try:
    while True:
        mensaje = input()

        if mensaje.lower() == "/exit":
            print("👋 Cerrando conexión...")
            client_socket.shutdown(socket.SHUT_RDWR)  # Detenemos entrada y salida
            client_socket.close()
            break

        client_socket.send(mensaje.encode("utf-8"))

except KeyboardInterrupt:
    print("\n⛔ Interrupción manual.")
    client_socket.close()

# Esperamos que el hilo receptor finalice
hilo_receptor.join()

print("✅ Cliente finalizado.")
