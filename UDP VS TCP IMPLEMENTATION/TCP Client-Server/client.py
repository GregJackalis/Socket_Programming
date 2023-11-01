import socket

FORMAT = 'utf-8'  # same here just like in server.py, I use this to send and receive messages in the same format
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is used basically to connect to the server, by passing the server's info
client.connect( (socket.gethostbyname(socket.gethostname()), 9095))

client.send("Hello Server!".encode(FORMAT))
print(client.recv(1024).decode(FORMAT))

client.send("This is my last message server...Byeee".encode(FORMAT))
print(client.recv(1024).decode(FORMAT))