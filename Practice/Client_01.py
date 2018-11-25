import socket

HOST = socket.gethostbyname("")
PORT = 7575

option01 = "Dennis"
option02 = "Close"
option03 = "Default"

while True:

    print("Choose what to send: ")

    print("\t(1)", option01)
    print("\t(2)", option02)

    answer = input()

    if answer is '1':
        msg = option01
    elif answer is '2':
        msg = option02
    else:
        msg = option03

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg.encode())
        data = s.recv(1024)

    print('Received:', repr(data))

    print(msg)

    if msg == option02:
        print("Closing Client Application...")
        break

