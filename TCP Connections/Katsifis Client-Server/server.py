import socket

# we do the same steps each time for socket programming:
# 1) we import the socket library (and all the libraries required, in this case the socket is enough)


# 2) Create s server socket
serverSocket = socket.socket()
print("Server socket created")


# 3) Associate the server socket with IP and Port
ip = socket.gethostbyname(socket.gethostname())
port = 35390

serverSocket.bind( (ip, port) )  # we need to put them in paretheses beacuse ip and port work together as coordinate 
# otherwise we could have also made a variable:
# addresss = (ip, port)
# serverSocket.bind(addresss)
print("Server socket bounded with IP {} and {} port".format(ip, port))


# 4) Make the server listen to incoming connections
serverSocket.listen()


# 5) Server incoming connections one at a time
count = 0  # it is a good practice to use a counter in order to count the number of messages the server receives
while True:
    (clientConnection, clientAddress) = serverSocket.accept()
    count += 1
    print("Accepted {} connections so far".format(count))

    # Ready to read from client connection
    while True:
        data = clientConnection.recv(1024)
        print(data)
        if data!=b'':
            msg1 = "hello client, i read everything you sent"
            msg1Bytes = str.encode(msg1)


            msg2 = "Now I will close connection"
            msg2Bytes = str.encode(msg2)

            clientConnection.send(msg1Bytes)
            clientConnection.send(msg2Bytes)

            print("Closing connection...")
            break
