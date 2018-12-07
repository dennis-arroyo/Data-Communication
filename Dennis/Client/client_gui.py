from tkinter import *
import random
import socket
import time
from _thread import *

HOST = socket.gethostname()
PORT = 7575

count = 0

playerName = ""

players = {}

textFieldContent = ""

score = ""


def game_instructions():
    return "Intructions:" \
           "\n1. Enter your username below and click connect to enter the game." \
           "\n2. Wait for connection of other players" \
           "\n3. When ready, click start game." \
           "\n4. The goal of the game is to click the showned images as quickly as possible" \
           "\n5. All players are going to receive the coordinates of all rounds" \
           "\n6. The server is going to analyze the results and crown the winner"


def goal_click():
    goal.place(x=random.randrange(50, windowWidth/2), y=random.randrange(50, windowHeight))
    global count
    count += 1
    if count >= 4:
        root.destroy()
        label = Label(rightFrame, text="You Win!", bg="White", fg="Green")
        label.place(x=425, y=100)
        label.pack
        win = Button(rightFrame, text="Exit", bg="red", fg="white", command=rightFrame.destroy)
        win.place(x=425, y=300)
        win.pack


# def init_connection():
#     global playerName
#     playerName = inputField.get()
#     if playerName is not "":
#         connectButton.destroy()
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             print(HOST)
#             s.connect((HOST, PORT))
#
#             s.sendall(playerName.encode())
#
#             # goal = Button(rightFrame, text="Start", bg="red", fg="white", command=goal_click)
#             # photo = PhotoImage(file='Pi.PNG')
#             # goal.config(image=photo)
#             # goal.pack()
#             # goal.place(x=random.randrange(0, windowWidth / 2), y=random.randrange(0, windowHeight))
#
#             # button = Button(leftBottom, text="Refresh", fg="#f2dde4", command=refresh_data)
#             # button.grid(row=3, column=0, pady=(10, 10))
#
#             # textbox.config(state=NORMAL)
#             # textbox.insert(END, data + " connected" + '\n')
#             # textbox.config(state=DISABLED)
#
#             data = s.recv(1024)
#             textbox.config(state=NORMAL)
#             textbox.insert(END, data.decode() + " connected" + '\n')
#             textbox.config(state=DISABLED)

def update_player_name():
    global playerName
    playerName = inputField.get()

    textbox.config(state=NORMAL)
    textbox.insert(END, playerName + " connected" + '\n')
    textbox.config(state=DISABLED)

    if playerName is not "":
        textFieldContent
        refresh = Button(leftBottom, text="Refresh", fg="#f2dde4", command=update_get_info)
        refresh.grid(row=3, column=0, pady=(10, 10))

        start_new_thread(socket_listener, (playerName, (HOST, PORT)))


def update_get_info():
    global textFieldContent

    textbox.config(state=NORMAL)
    textbox.insert(END, textFieldContent + " connected" + '\n')
    textbox.config(state=DISABLED)


def socket_listener(player, physicalAddress):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((physicalAddress[0], physicalAddress[1]))

        s.sendall(player.encode())

        while True:

            time.sleep(1.5)

            global getInfo
            global textFieldContent
            global score

            if score is not "":
                s.sendall(score.encode())
                data = s.recv(1024)
                textFieldContent = data.decode()
                print(textFieldContent)
                score = ""
            else:
                s.sendall(b"refresh")
                textFieldContent = s.recv(1024)
                textbox.config(state=NORMAL)
                textbox.delete('1.0', END)
                textbox.insert(END, textFieldContent.decode() + " connected" + '\n')
                textbox.config(state=DISABLED)

# def refresh_data():
#     data = s.recv(1024)
#     textbox.config(state=NORMAL)
#     textbox.insert(END, data.decode() + " connected" + '\n')
#     textbox.config(state=DISABLED)


root = Tk()

root.configure(background='#17090e')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
windowWidth = 950
windowHeight = 650
size = "950x700"
x = w / 2 - windowWidth / 2
y = h / 2 - windowHeight / 2

root.geometry("950x700+%d+%d" % (x, y))

root.resizable(0, 0)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=(0, 2))

leftFrame.configure(background='black')

rightFrame = Frame(root, bg="#b3446c", width=windowWidth/2)
rightFrame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

leftTop = Frame(leftFrame)
leftTop.pack(side=TOP, fill=BOTH, expand=TRUE, pady=(0, 2))

leftBottom = Frame(leftFrame, bg="#f2dde4")
# leftBottom = Frame(leftFrame, bg="#847479")
leftBottom.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

# textbox = Text(leftTop, bg="#8b44b3", fg="#44b38b")
textbox = Text(leftTop, fg="#44b38b")
textbox.pack(fill=BOTH, expand=TRUE)
textbox.place(x=0, y=0)


for player in players:
    textbox.insert(END, player + " connected" + '\n')
    print(textbox.get(1.0, END))

textbox.config(state=DISABLED)

instructions = Label(leftBottom, text=game_instructions(), font=("Times New Roman", 14),
                     justify=LEFT, bg="#f2dde4", fg="#080305")
instructions.grid(row=0, column=0, pady=(50, 10))

label = Label(leftBottom, text="Enter Username:", font=("Times New Roman", 18), bg="#f2dde4")
label.grid(row=1, column=0, pady=(10, 10))

inputField = Entry(leftBottom, text="Username...", width=50)
inputField.grid(row=2, column=0, pady=(10, 10))

connectButton = Button(leftBottom, text="Connect", fg="#f2dde4", command=update_player_name)
connectButton.grid(row=3, column=0, pady=(10, 10))

root.mainloop()

