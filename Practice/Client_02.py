import socket

# HOST = '127.0.0.1'

HOST = socket.gethostbyname("")
PORT = 7575

print("Choose what to send: ")

print("(1) Hello World")
print("(2) Close")

answer = input()

if answer is '1':
    msg = 'Hello World'
elif answer is '2':
    msg = 'Close'
else:
    msg = "Default"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.send(b'Hello Dennis')
    s.send(msg.encode())
    data = s.recv(1024)

print('Received:', repr(data))
