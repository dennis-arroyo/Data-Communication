import socket
from _thread import *

HOST = socket.gethostname()
PORT = 7575


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        obj = s.accept()
        connection, address = obj
        # connection.sendall(b"Connection Successful")
        data = connection.recv(1024).decode()
        print(data)
        connection.sendall(data.encode())
