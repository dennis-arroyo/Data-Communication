import socket
from _thread import *

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")

# Pixel's raspberry pi ip address
# HOST = "192.168.43.83"

# Home router raspberry pi ip address
# HOST = "192.168.8.166"

PORT = 7575

clients = {}
# player = 1
text_field = "Players \t\tScore \t\tPosition\n\n"
player = ""
score = "0"


def client_thread(conn, add, cl):
    while True:

        global score

        data = conn.recv(1024)
        reply = data.decode()
        print(type(reply))
        # print(cl[add])
        if not data:
            break
        if reply == "45":
            cl[add][1] = reply
        else:
            extracted_players = [value for key, value in cl.items()]

            players = ""

            # for pl in extracted_players:
            #     players += pl + ","

            for p in extracted_players:
                players += p[0] + "\t\t" + p[1] + "\t\t" + p[2] + "\n"

            conn.sendall(players.encode())


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
        player = connection.recv(1024)
        # print(player.decode())
        concatenated_address = address[0] + ":" + str(address[1])
        clients[concatenated_address] = [player.decode(), "0", "null"]
        # print(clients)
        start_new_thread(client_thread, (connection, concatenated_address, clients))
