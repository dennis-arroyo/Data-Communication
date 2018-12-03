from tkinter import *
import random

count = 0


def goalClick():
    goal.place(x=random.randrange(50, 800), y=random.randrange(50, 550))
    global count
    count += 1
    if count >= 4:
        goal.destroy()
        label = Label(mw, text="You Win!", bg="Green")
        label.place(x=425, y=100)
        label.pack
        win = Button(mw, text="Exit", bg="red", fg="white", command=mw.destroy)
        win.place(x=425, y=300)
        win.pack






mw = Tk()

mw.geometry("850x600")
mw.resizable(0, 0)

players = ["Angel", "Dennis"]

textbox = Text(mw)
textbox.pack()
textbox.place(x=0 , y=0)

for player in players:
    textbox.insert(END, player + " connected"+'\n')
    print(textbox.get(1.0, END))




goal = Button(mw,text="Start", bg="red", fg="white",command=goalClick)
goal.pack()
goal.place(x=random.randrange(0,850), y=random.randrange(0,600))








mw.mainloop()