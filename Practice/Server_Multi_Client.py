import socket
from _thread import *

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")

PORT = 7575

clients = {}
# player = 1
player = ""


def client_thread(conn, add, cl):
    while True:
        data = conn.recv(1024)
        reply = data.decode()
        if not data:
            break
        print(cl[add[0] + ":" + str(add[1])] + ": " + reply)
        print("\t", cl)
        current_add = add[0] + ":" + str(add[1])
        other_clients_list = other_clients(cl, current_add)

        print(other_clients_list)

        for c in cl:
            strn = "Sending message to --> " + c[0] + ":" + str(c[1])
            conn.sendto(strn.encode(), (c[0], int(c[1])))


def other_clients(cl, current_address):
    addresses = [key for key, value in cl.items() if key not in current_address]
    print("\t\t", addresses)
    ip_and_port = []

    for a in addresses:
        ip, p = a.split(":")
        ip_and_port.append([ip, int(p)])

    return ip_and_port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        obj = s.accept()
        connection, address = obj
        # clients[address[0] + ": " + str(address[1])] = "Player #" + str(player)
        player = connection.recv(1024)
        clients[address[0] + ":" + str(address[1])] = player.decode()
        # player += 1
        start_new_thread(client_thread, (connection, address, clients))
