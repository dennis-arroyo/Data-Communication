import socket
from _thread import *

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")

PORT = 7575

clients = {}
player = 1

def client_thread(conn, add, cl):
    while True:
        data = conn.recv(1024)
        reply = "Server Connection Successful: " + data.decode()
        if not data:
            break
        print(cl[add[0] + str(add[1])] + ": " + reply)
        print("\t", add)
        conn.sendall(reply.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        obj = s.accept()
        connection, address = obj
        clients[address[0] + str(address[1])] = "Player #" + str(player)
        player += 1
        start_new_thread(client_thread, (connection, address, clients))
