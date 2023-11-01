import socket

# if the server is only going to be working on this internet/wifi through this computer then we can just use this:
# HOST = 'localhost' OR '127.0.0.1'
HOST = socket.gethostbyname(socket.gethostname())

# For ports we shoudn't use a low number because those are often used by the computer and other operations
PORT = 9090

# First parameter is the type of socket, second one is about TCP or UDP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))  # it needs to be a tuple!!

# the 5 means that if more than 5 connections are waiting, then it will reject newer connections (it's like limiting the server's connections)
server.listen(5)

while True:  # this is uncoditional, it's always accepting
    communication_socket, address = server.accept()
    # what this method is doing is that we're waiting for a client to connect, and if one does then the .accpet() returns
    # the address from which the client is sending and also a socket which we can use in order to talk back to that client
    # We so NOT use the server socket to talk with the client!!

    print("[CONNECTED] A new connection was made to address: {}".format(address))

    # when sending messages, we need to encode the in to bytes becuase we're using bytes-streams
    message = communication_socket.recv(1024).decode('utf-8')
    print("[CLIENT MESSAGE] Client from address {} sends:\n{}".format(
        address, message))

    # Be careful when using the .send and the encode/decode functions! The .encode and .decode
    # methods go INSIDE the parentheses of the .send() function, and NOT OUTSIDE
    communication_socket.send(
        "[SERVER] The server received your message succesfully! Thank you!".encode('utf-8'))

    # Closing the connection with the client, since SOCK_STREAM is used.
    # We close it by closing the socket used to comminicate with the client
    communication_socket.close()
    print(f"Connection with {address} ended!")
