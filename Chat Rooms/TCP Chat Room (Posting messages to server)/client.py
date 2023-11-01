import socket
import threading

FORMAT = 'utf-8'

clientSide = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now instead of binding a socket to an address and a port, we just connect it to the server straigh ahead
clientSide.connect((socket.gethostbyname(socket.gethostname()), 50510))

# using again a receive method (used as a main method as well) in order to always try (while connected) and receive a message from the
# server, which that message can either be the server saying that the client has succesfully connected or more importantly, the server
# broadcasting another client's message
def receive():
    while True:
        try:
            serverMessage = clientSide.recv(1024).decode(FORMAT)

            print(serverMessage)

            # Now we need while the client keeps waiting, to check if the server sends a specific message:
            # if the message sent is "[SERVER] Insert Nickanme:", then by splitting the words based 
            # on blank spaces and storing them into a list, then the second element (list[1]) will be "Insert"
            # NOT NEEDED (for now at least)
            # if serverMessage.split(' ')[1] == "Insert":  
            #     clientSide.send(input("here: \n").encode(FORMAT))
        except:
            print("An error occurred!")
            clientSide.close()
            break


def write():
    while True:
        message = f'{input(" ")}'
        clientSide.send(message.encode(FORMAT))


# now we need to run two threads, one for receiving and one for the write function
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()