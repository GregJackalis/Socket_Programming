import socket

FORMAT = 'utf-8'

# In this case, because UDP is a connection-less socket stream protocol it uses datagrams, so in the second parameter we pass in SOCK_DGRAM
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# We still need to bind to a server and a port
server.bind((socket.gethostbyname(socket.gethostname()), 9096))

# BUT, we will NOT NEED the .listen and .accpet functions because we're not listening and accepting connections, we're just listening for messages
# coming in. That's why we just use this:
# the message and the address that is received from are saved in the two variables here
message, address = server.recvfrom(1)
print(message.decode(FORMAT))

# if the buffer size is not enough to store the whole message that is sent from the client, then the whole message will be
# dropped/rejected, whereas in TCP it will just "split" the message and send it sequentially

# NOTE: We can also still use the.recv method but because this socket is connection-less, we won't know the address/where the message
#       is coming from, so in that case we won't be able to send anything back (like a confirmation message etc).
#       With the .recvfrom() method we also get the address

server.sendto(
    "[SERVER] Hello Client! Your message was received succesfully!".encode(FORMAT), address)  # the address is where the client is


# NOTICE how there is no Communication Socket to be closed, no connection to be close! This is because the message was received then
# a message was sent back and not any connection was actually established between the server and the client.
# So since in the first place no real connection was made, then there isn't a connection to be closed.
# The server will just be an open endpoint waiting to just receive indepedent messages and then possible (and usually that's how it goes)
# send something back
