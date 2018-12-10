import socket
import random
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
        # print(cl[add])
        if not data:
            break
        if reply == "45":
            cl[add][1] = reply
        else:
            extracted_players = [value for key, value in cl.items()]

            players = ""

            for p in extracted_players:
                players += p[0] + "\t\t" + p[1] + "\t\t" + p[2] + "\n"

            conn.sendall(players.encode())


def get_numbers(orientation):
    numbers = str(random.randrange(orientation))

    counter = 0

    while counter < 5:
        numbers += "," + str(random.randrange(orientation))
        counter += 1

    return numbers


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    x = get_numbers(475)
    y = get_numbers(650)

    while True:
        obj = s.accept()
        connection, address = obj
        player = connection.recv(1024)
        connection.sendall((x + "-" + y).encode())
        concatenated_address = address[0] + ":" + str(address[1])
        clients[concatenated_address] = [player.decode(), "0", "null"]
        start_new_thread(client_thread, (connection, concatenated_address, clients))
