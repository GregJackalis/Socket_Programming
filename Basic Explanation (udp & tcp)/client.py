import socket

# We need to use the same ip as the server (if the client and the server are connected in the same LAN)
# BUT if the client lets say is outside the Local Area Network, then on the address it needs to use
# the public IP address of the LAN where the server is, which can be found on myip.is website
HOST = socket.gethostbyname(socket.gethostname())

# The port needs to also be the same
PORT = 9090

# Making the client socket, again with the same "settings". Internet socket AF_INET and TCP protocol SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Instead of .bind() we use the .connect on clients and we pass in again the HOST and PORT variables as a tuple/pair
client.connect((HOST, PORT))

# We're sending the server a message
client.send("Hello Server!".encode('utf-8'))

# Printing the response the server sends back
print(client.recv(1024).decode('utf-8'))


# NOTE: We only use ONE socket here in order to receive and send messages into a server. Whereas on the server side, we have one socket
#       for the server starting up and working, and one socket for the connection with a client
