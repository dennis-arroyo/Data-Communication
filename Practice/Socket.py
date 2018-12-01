import socket
from _thread import *

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")

PORT = 7575

clients = {}
connections = []
# player = 1
player = ""


def client_thread(conn, add, cl):
    while True:
        data = conn.recv(1024)
        reply = data.decode()
        if not data:
            break
        else:
            for c in cl:
                print(c)
                c.sendall(reply.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        obj = s.accept()
        connection, address = obj
        print(connection)
        # clients[address[0] + ": " + str(address[1])] = "Player #" + str(player)
        player = connection.recv(1024)
        clients[address[0] + ":" + str(address[1])] = player.decode()
        connections.append(connection)
        # player += 1
        start_new_thread(client_thread, (connection, address, connections))
