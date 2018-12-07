import socket

HOST = socket.gethostname()
PORT = 7575

SOCKET = socket.gethostname()
PORT_NEW = 9090


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        msg = input()

        data = s.recv(1024)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
            s2.bind((HOST, PORT))
            s2.listen()
            s2.sendall(b"Connection Successful")

        print('Received:', repr(data))

        print(msg)
