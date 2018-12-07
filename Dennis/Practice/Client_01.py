import socket
import time

HOST = socket.gethostname()
PORT = 7575

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    i = 0

    while True:

        time.sleep(1.5)
        s.sendall(str(i).encode())
        data = s.recv(1024)

        print('Received:', int(data.decode()))

        i += 1

