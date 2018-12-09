import socket

HOST = socket.gethostname()
PORT = 7575


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        obj = s.accept()
        connection, address = obj
        data = connection.recv(1024).decode()
        print(data)
        connection.sendall(data.encode())


