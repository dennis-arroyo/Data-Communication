import socket

HOST = socket.gethostbyname("")
PORT = 7575

playerName = input("Enter your name to start connection:")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(playerName.encode())

    while True:

        msg = input()

        s.sendall(msg.encode())
        data = s.recv(1024)

        print('Received:', repr(data))

        print(msg)
