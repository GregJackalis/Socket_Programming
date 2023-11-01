import socket
import time  # for detail purposes, nothing else

# With the TCP protocol we want to use a Connection-Oriented Socket, meaning a connection is established between client and server
# and this connection is used to exchange information
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind( (socket.gethostbyname(socket.gethostname()), 9095))

FORMAT = 'utf-8'  # this is a constant variable that is used when we want to decode or encode messages and send them from one side to another

server.listen()

while True:
    client_socket, address = server.accept()  # first var is the new socket made that is used to communicate with the client
    print(f"Connected to {address}")

    # NOTE: Deadlock situation is when both sides are waiting to receive something so nothing is happening and both of them remain idle

    message = client_socket.recv(1).decode(FORMAT)  # the 1024 number which is the size of bytes we can receive from one message (aka buffer size)
    # For TCP this number is not as important as in UDP, because in UDP there can be packet and/or byte-loss, we can "restrict" that
    # by using a very small number of accepted bytes. In case in UDP a message of larger amount of bytes is sent compared to the parameter,
    # then the whole message will be dropped/rejected. 
    # Whereas as we already know with TCP, packet loss is not allowed therefore in
    # case it happens then both of the server and client as informed about it
    print(f"[CLIENT] Client sends:\n\"{message}\"")

    # Sending back to the client a message verifying that their message got received
    client_socket.send("[SERVER] Server says: \"Hello Client! Your message was received succesfully!\"".encode(FORMAT))

    time.sleep(4)  # used this so that it's noticable when the server close connection

    client_socket.send("[SERVER] Closing Connection...Bye!".encode(FORMAT))
    client_socket.close()