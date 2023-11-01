import threading
import socket
import time  # used for detail purposes


FORMAT = 'utf-8'

host = socket.gethostbyname(socket.gethostname())  # or using '127.0.0.1' for localhost
port = 50510

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # internet socket and TCP type socket is made here
server.bind( (host, port) )

server.listen()

clients = []
nicknames = []

# using this function to make the code less chaotic and more readable. This function is used to 
# handle the case where a client has pressed Control+C on their terminal
def handle_disconnected_client(comm_Sock):
    index = clients.index(comm_Sock)
    clients.remove(comm_Sock)
    comm_Sock.close()
    nickname = nicknames[index]
    broadcast(f"[SERVER] {nickname} has left the chat\n")
    print(f"[CLIENT] Client {nickname} has lost connection!")
    nicknames.remove(nickname)


# DEFINING METHODS:

# 1) Broadcast function (sending a message to all the clients that are currently connected in the server)
def broadcast(message):
    for client in clients:
        client.send(message.encode(FORMAT))


# 2) Receiving a message from a client and then process it and send it to the other clients:
# what this function does is that in case a client sends a message, it receives it and then sends it to the rest of the clients
# and if an error is returned (let's say the client leaves the chat room) then the client is removed from the lists and the 
# thread (the while loop) that we made gets broken
def handle(comm_Sock):
    while True:
        try:
            userMessage = comm_Sock.recv(1024).decode(FORMAT)
            if not userMessage: raise ConnectionResetError
            userIndex = clients.index(comm_Sock)
            nick_ = nicknames[userIndex]
            broadcast(f"[{nick_}]: {userMessage}")
        except ConnectionResetError:
            handle_disconnected_client(comm_Sock)
            break
    

# 3) Defining a main method (the receive method) that combines all of the things that we've written till now
def receive():
    while True:
        communication_Socket, address = server.accept()  # as we already know the .accept() will return a communcation socket and the client's address
        print(f"[CLIENT {address}] Client has been connected!")  # this will NOT be broadcasted into the other users,
                                                                             # it's only used to print to the server

        # asking the client for a nickname
        communication_Socket.send("[SERVER] Insert a Nickname: ".encode(FORMAT))
        user_nickname = communication_Socket.recv(1024).decode(FORMAT)

        # adding nickname and client info (communication socket) to the previously made lists
        nicknames.append(user_nickname)
        clients.append(communication_Socket)

        # printing on the server side the nickname of the currently joined client, then broadcasting a message with the nickname
        print(f"[CLIENT {address}] Nickname for Client is: {user_nickname}\n")

        # sending a "verification message" back to the client saying that they have succesfully connected to the server
        communication_Socket.send("[SERVER] Succesfully connected to server!\n".encode(FORMAT))

        broadcast(f"[SERVER] {user_nickname} has joined the chat room!\n")
        
        

        # using threading to process messages and requests at the same time (roughly) from more than one client
        # each client has their own thread running
        thread = threading.Thread(target=handle, args= (communication_Socket,))  # the target function is the handle function that checks if a client sends a message
        thread.start()                  # NOTE: Remember to always use a tuple when passing arguments for a function inside the .Thread method


print("Server is listening...")
receive()  # calling the receive (also our main method) in order for the scipt to actually start running and wait for a client to be conencted