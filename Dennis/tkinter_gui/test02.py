from tkinter import *



root = Tk()

topFrame = Frame(root, bg="red")
bottomFrame = Frame(root)

label = Label(topFrame, text="Click button below:")
button1 = Button(bottomFrame, text="Click Me", fg="purple")
button2 = Button(bottomFrame, text="Click Me", fg="purple")

label.pack()

button1.pack(side=LEFT)
button2.pack(side=LEFT)

topFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)

root.mainloop()