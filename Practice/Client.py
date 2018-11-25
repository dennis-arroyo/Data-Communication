import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostbyname("") # Get local machine name
port = 12345                    # Reserve a port for your service.

s.connect((host, port))

print( s.recv(1024) )

s.close                          # Close the socket when done