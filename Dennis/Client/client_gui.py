from tkinter import *
import socket
import time
from _thread import *

# HOST = socket.gethostbyname("")

# Pixel's raspberry pi ip address
HOST = "192.168.43.83"

# Home router raspberry pi ip address
# HOST = "192.168.8.166"

PORT = 7575

count = 0

playerName = ""

players = {}

textFieldContent = ""

score = ""

text_field = "Players \t\tScore \t\tPosition\n\n"

coordinates_x = ""
coordinates_y = ""
x_coordinates_values = ""
y_coordinates_values = ""
coordinates_counter = 0

timer_start = 0
timer_end = 0
time_difference = 0


def game_instructions():
    return "Intructions:" \
           "\n1. Enter your username below and click connect to enter the game." \
           "\n2. The goal of the game is to click the showed images as quickly as possible" \
           "\n3. All players are going to receive the same coordinates of the images" \
           "\n4. After finishing the game, the server will send the scores of the players"


def goal_click():
    global x
    global y
    global coordinates_counter
    global timer_end
    global time_difference

    goal.place(x=int(x_coordinates_values[coordinates_counter]), y=int(y_coordinates_values[coordinates_counter]))
    coordinates_counter += 1
    if coordinates_counter >= 10:
        goal.destroy()
        timer_end = time.time()
        time_difference = round(timer_end - timer_start, 2)
        send_score_bottom = Button(leftBottom, text="Send Results", fg="#f2dde4", command=send_score)
        send_score_bottom.grid(row=3, column=0, pady=(10, 10))
        score_field = Label(leftBottom, text="You finished the game in: " + str(time_difference) + "seconds",
                            font=("Times New Roman", 18), bg="#f2dde4")
        score_field.grid(row=4, column=0)


def update_player_name():
    global playerName
    global timer_start

    playerName = inputField.get()

    if playerName is not "":
        connectButton.destroy()

        timer_start = time.time()

        start_new_thread(socket_listener, (playerName, (HOST, PORT)))


def send_score():
    global time_difference
    global score
    score = "get_score"


def socket_listener(player, physicalAddress):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        global coordinates_x
        global coordinates_y
        global x_coordinates_values
        global y_coordinates_values
        global coordinates_counter
        global score

        s.connect((physicalAddress[0], physicalAddress[1]))

        s.sendall(player.encode())

        coordinates = s.recv(1024)

        coordinates_x, coordinates_y = coordinates.decode().split("-")

        x_coordinates_values = coordinates_x.split(",")
        y_coordinates_values = coordinates_y.split(",")

        goal.grid()
        goal.place(x=int(x_coordinates_values[coordinates_counter]), y=int(y_coordinates_values[coordinates_counter]))

        coordinates_counter += 1

        while True:

            time.sleep(1.5)

            global getInfo
            global textFieldContent
            global score

            if score is not "":
                s.sendall(score.encode())
                s.sendall(str(time_difference).encode())
                score = ""
            else:
                s.sendall(b"refresh")
                textFieldContent = s.recv(1024)
                format_field_content = textFieldContent.decode().split(",")
                textbox.config(state=NORMAL)
                textbox.delete('1.0', END)
                textbox.insert(END, text_field)
                for content in format_field_content:
                    textbox.insert(END, content + '\n')
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
leftFrame.pack(side=LEFT, fill=BOTH, expand=FALSE, padx=(0, 2))

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


textbox.config(state=DISABLED)

instructions = Label(leftBottom, text=game_instructions(), font=("Times New Roman", 14),
                     justify=LEFT, bg="#f2dde4", fg="#080305")
instructions.grid(row=0, column=0, pady=(50, 10))

label = Label(leftBottom, text="Enter Username:", font=("Times New Roman", 18), bg="#f2dde4")
label.grid(row=1, column=0, pady=(10, 10))

inputField = Entry(leftBottom, text="Username...", width=50)
inputField.grid(row=2, column=0, pady=(10, 10))

connectButton = Button(leftBottom, text="Connect", fg="black", command=update_player_name)
connectButton.grid(row=3, column=0, pady=(10, 10))

photo = PhotoImage(file='raspberry.PNG')
goal = Button(rightFrame, image=photo, width=120, height=120, bg="#b3446c", fg="white", command=goal_click)

root.mainloop()

