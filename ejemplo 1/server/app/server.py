import socket
import threading
import os

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
            cliente.sendall("archivo recibido")
            cliente.close()



if __name__=="__main__":
    server(49000)