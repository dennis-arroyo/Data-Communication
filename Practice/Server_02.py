import socket

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")

PORT = 7575

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # connection, address = s.accept()   ####################################################
#                                        If this is implemented outside the while True,
    # with connection:                   it only listens for one connection and ends program.
    #     print('Connected by', address) ####################################################

    while True:
        connection, address = s.accept()

        with connection:
            print('Connected by', address)

            data = connection.recv(1024)

            if not data:
                break

            print(data.decode())
            connection.sendall(data)

            if data.decode() == "Close":
                print("Closing program...")
                break
