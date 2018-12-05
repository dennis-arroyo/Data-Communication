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

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

root.geometry("850x600+"+str(positionDown)+"+"+str(positionRight))
root.resizable(0, 0)

frame = Frame(root, width=800)
bottomFrame = Frame(root, width=860)

# leftFrame.grid(row=0, column=0)
# rightFrame.grid(row=1, column=0)

frame.pack()
bottomFrame.pack(side=BOTTOM)

title = Label(frame, text="SOME GAME", font=("Arial", 25))
title.grid(row=0, column=0)

instructions = Label(frame, text=game_instructions(), font=("Times New Roman", 18), anchor=W, justify=LEFT)
instructions.grid(row=1, column=0)

divisionLine = Frame(frame, height=1, width=800)
divisionLine.grid(row=2, column=0, pady=80)

label = Label(bottomFrame, text="Enter Username:", font=("Times New Roman", 20))
label.grid(row=0, column=0)

inputField = Entry(bottomFrame, text="Username...", width=50)
inputField.grid(row=1, column=0)

button = Button(bottomFrame, text="Connect")
button.grid(row=2, column=0)

root.mainloop()
