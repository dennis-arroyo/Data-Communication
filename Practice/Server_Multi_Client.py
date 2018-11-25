import socket

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")

PORT = 7575

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        obj = s.accept()
        connection, address = obj

        with connection:
            data = connection.recv(1024)

            print("\n", data.decode())
            print('\tConnected by', address)

            connection.sendall(data)

            if data.decode() == "Close":
                print("Closing program...")
                break
