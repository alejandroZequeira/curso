import socket

def enviar_archivo(nombre_archivo, cliente):
    with open(nombre_archivo, 'rb') as archivo:
        datos = archivo.read()
        cliente.sendall(datos)

def client(host,port,nombre_archivo):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    enviar_archivo(nombre_archivo, client_socket)
    mensaje=client_socket.recv(1024)
    print("mensaje del servidor: ",mensaje)

   
if __name__ == "__main__":
    client("server",49000,"mensaje.txt")
