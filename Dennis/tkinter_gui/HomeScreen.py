from tkinter import *


def game_instructions():
    return "Intructions:" \
           "\n1. Enter your username below and click connect to enter the game." \
           "\n2. Wait for connection of other players" \
           "\n3. When ready, click start game." \
           "\n4. The goal of the game is to click the showned images as quickly as possible" \
           "\n5. All players are going to receive the coordinates of all rounds" \
           "\n6. The server is going to analyze the results and crown the winner"


root = Tk()

leftFrame = Frame(root)
rightFrame = Frame(root)

instructions = Label(leftFrame, text=game_instructions(), font=("Times New Roman", 12), anchor=W, justify=LEFT)
instructions.grid(row=0, column=0)

divisionLine = Frame(leftFrame, height=50, width=1, bg="black")
divisionLine.grid(row=0, column=1)

label = Label(rightFrame, text="Enter Username:", font=("Times New Roman", 12))
label.grid(row=0, column=0)

inputField = Entry(rightFrame)
inputField.grid(row=1, column=0)

button = Button(rightFrame, text="Connect")
button.grid(row=2, column=0)

leftFrame.grid(row=0, column=0)
rightFrame.grid(row=0, column=1)

root.mainloop()
