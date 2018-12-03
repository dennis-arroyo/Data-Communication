from tkinter import *

root = Tk()

# Label(Tk(), text="some text")
label = Label(root, text="Dennis")

# Pack it in the first place it sees
label.pack()

# Makes window continue to be on screen. Without it, it pops up and closes.
# Infinite loop to continue to display window until desired action is done.
root.mainloop()
