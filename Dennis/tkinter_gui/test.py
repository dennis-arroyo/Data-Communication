from tkinter import *

root = Tk()

leftFrame = Frame(root, width=200, height=500, bg="red")
leftFrame.pack(side=LEFT)

rightFrame = Frame(root, width=400, height=500, bg="blue")
rightFrame.pack(side=RIGHT)

leftTop = Frame(leftFrame, width=100, height=250, bg="yellow")
leftTop.pack(side=TOP)

leftBottom = Frame(leftFrame, width=100, height=250, bg="purple")
leftBottom.pack(side=BOTTOM)


root.mainloop()
