import socket 

# Same steps apply for the client side, with only minor differencies
# 1) Create client socket (socket instance)
socketObject = socket.socket()


# Use socket to connect to server, they need to both have the SAME IP AND PORT
ip = socket.gethostbyname(socket.gethostname())
port = 35390
socketObject.connect( (ip, port) ) 
print("Connected to localhost")


# Send message to web server to supply e.g. a web page
HTTPmessage = "GET / HTTP/1.1\r\n Host: localhost\r\n Connection: close\r\n\r\n"
msgBytes = str.encode(HTTPmessage)

socketObject.send(msgBytes)

# Receive Data
while True:
    data = socketObject.recv(1024)
    print(data)

    if data != b'':
        print("Connection Closed")
        break

socketObject.close()