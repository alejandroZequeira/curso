import socket
import threading
import os


def enviar_archivo(nombre_archivo, cliente):
    with open("data/"+nombre_archivo, 'rb') as archivo:
        datos = archivo.read()
        cliente.sendall(datos)

def server(port):
    host="0.0.0.0"
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as servidor:
        servidor.bind((host,port))
        servidor.listen()
        print(f"servidor en linea en:{host}:{port}")
        while True:
            cliente,direccion=servidor.accept()
            nombre_archivo = cliente.recv(1024).decode()
            print(f"conexion desde:{direccion}")
            print("Recibiendo archivo:", nombre_archivo)
            if not os.path.exists("data"):
                os.makedirs("data")
            with open("data/"+nombre_archivo, 'wb') as archivo:
                datos = cliente.recv(1024)
                archivo.write(datos)
            cliente.sendall("archivo recibido")
            cliente.close()



if __name__=="__main__":
    server(49000)