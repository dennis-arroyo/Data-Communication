import socket
import random
from _thread import *

# HOST = '127.0.0.1'

# HOST = socket.gethostbyname("")
HOST = socket.gethostname()

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
min_seconds = ["", "999999"]


def client_thread(conn, add, cl):
    while True:

        global score
        global min_seconds

        data = conn.recv(1024)
        reply = data.decode()
        # print(cl[add])
        if not data:
            break
        if reply == "get_score":
            seconds = conn.recv(1024).decode()
            cl[add][1] = seconds
            if float(seconds) < float(min_seconds[1]):
                min_seconds = []
                min_seconds.append(add)
                min_seconds.append(seconds)
                print("Max Score Address: " + min_seconds[0])

        else:

            if add == min_seconds[0]:
                cl[add][2] = "winning"
            else:
                cl[add][2] = "losing"

            extracted_players = [value for key, value in cl.items()]

            players = ""

            for p in extracted_players:
                players += p[0] + "\t\t" + p[1] + "\t\t" + p[2] + "\n"

            conn.sendall(players.encode())


def get_numbers(orientation):
    numbers = str(random.randrange(orientation))

    counter = 0

    while counter < 10:
        numbers += "," + str(random.randrange(orientation))
        counter += 1

    return numbers


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    x = get_numbers(455)
    y = get_numbers(590)

    while True:
        obj = s.accept()
        connection, address = obj
        player = connection.recv(1024)
        connection.sendall((x + "-" + y).encode())
        concatenated_address = address[0] + ":" + str(address[1])
        clients[concatenated_address] = [player.decode(), "0", "null"]
        start_new_thread(client_thread, (connection, concatenated_address, clients))
