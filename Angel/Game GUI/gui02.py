from tkinter import *
import random
import socket

count = 0

HOST = socket.gethostbyname("")
PORT = 7575

playerName = ""


def game_instructions():
    return "Intructions:" \
           "\n1. Enter your username below and click connect to enter the game." \
           "\n2. Wait for connection of other players" \
           "\n3. When ready, click start game." \
           "\n4. The goal of the game is to click the showned images as quickly as possible" \
           "\n5. All players are going to receive the coordinates of all rounds" \
           "\n6. The server is going to analyze the results and crown the winner"


def goal_click():
    goal.place(x=random.randrange(50, 800), y=random.randrange(50, 550))
    global count
    count += 1
    if count >= 4:
        goal.destroy()
        label = Label(mw, text="You Win!", bg="White", fg="Green")
        label.place(x=425, y=100)
        label.pack
        win = Button(mw, text="Exit", bg="red", fg="white", command=mw.destroy)
        win.place(x=425, y=300)
        win.pack


mw = Tk()

mw.geometry("850x600")
mw.resizable(0, 0)

players = ["Angel", "Dennis"]

textbox = Text(mw, width=35, height=10)
textbox.pack()
textbox.place(x=0, y=0)

for player in players:
    textbox.insert(END, player + " connected" + '\n')
    print(textbox.get(1.0, END))

goal = Button(mw, text="Start", bg="red", fg="white", command=goal_click)
photo = PhotoImage(file='Pi.PNG')
goal.config(image=photo)
goal.pack()
goal.place(x=random.randrange(0, 850), y=random.randrange(0, 600))

instructions = Label(mw, text=game_instructions(), font=("Times New Roman", 14), anchor=W, justify=LEFT)
instructions.pack()
instructions.place(x=0, y=200)

enterUserName = Label(mw, text="Enter Username Below to connect:")
enterUserName.pack()
enterUserName.place(x=0, y=400)

textInput = Entry(mw)
textInput.pack()
textInput.place(x=0, y=425)

verticalDivision = Frame(mw, height=600, width=2, bg="black")
verticalDivision.pack()
verticalDivision.place(x=490, y=0)

horizontalDivision = Frame(mw, height=2, width=490, bg="black")
horizontalDivision.pack()
horizontalDivision.place(x=0, y=200)

if playerName is not "":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall(playerName.encode())

        while True:

            msg = input()

            s.sendall(msg.encode())
            data = s.recv(1024)

            print('Received:', repr(data))

            print(msg)

mw.mainloop()
