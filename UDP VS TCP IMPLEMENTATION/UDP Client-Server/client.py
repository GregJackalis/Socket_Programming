import socket

FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Here, because there is no connection, for the second parameter of the .sendto() method we need to use a tuple in which
# the server's address and port are in. This is used so that the program knows the place/address (in general) it will send the message
client.sendto("[CLIENT] Hello Server!".encode(FORMAT),
              (socket.gethostbyname(socket.gethostname()), 9096))  # using the .gethostbyname because both scripts are in the same computer

# Now here, with the recvfrom we get a tuple of the message and where the message is coming from/where the socket is located.
# so we need to use it as a list and therefore return the First Element of the tuple, meaning the element with the index 0
print(client.recvfrom(1024)[0].decode(FORMAT))
