import socket
import threading
import queue  # importing the queue data structure because we can't store and have an order for messages in UDP

FORMAT = 'utf-8'

messages = queue.Queue()
clients = []
nicknames = []

# defining a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostbyname(socket.gethostname()), 9095))

print("Server is open...")


def handle_disconnect(exit_name):
    for client in clients:
        server.sendto(f"{exit_name} has left the chat!".encode(FORMAT), client)


# this function will receive and accept messages while also storing them inside a queue data structure
def receive():
    while True:
        try:
            client_Message, address = server.recvfrom(1024)
            messages.put((client_Message, address))
        except:
            pass


# this function will be used to broadcast messages to all the users. after each message is received through a while true loop
# and its put inside the messages queu, then each of that tuple added to the queue, will be taken out using the .get() method
# and then checking if the client is in the client list. Then the client list will have stored varius addresses from different clients
# and we will use them to send back messages with the .sendto() method that takes the message for the first parameter and the address
# that the message will be sent to- as the second argument
def broadcast():
    while True:
        name = ""
        while not messages.empty():  # while the messages queue is NOT empty
            try:
                # we use the .get() method to remove and store here in two variables the values inside the tuple-inside the queue
                message, addr = messages.get()
                # then if the address that is inside the messages queu (so an adddress that sent a message) is NOT in the clients list
                if addr not in clients:
                    # then it is added to the list, which this list has the addresses of each client that will be later used to directly send a message to them
                    clients.append(addr)

                index = clients.index(addr)
                for client in clients:
                    # if the message sent starts with this word then a nickname is given
                    if message.decode(FORMAT).split(' ')[0] == "Nickname:":
                        name = message.decode(FORMAT).split(' ')[1].strip("'")
                        print(f"{name} has been connected!")
                        # here we use the address from the clients list to send a message directly
                        server.sendto(
                            f"{str(name)} has joined the chat!".encode(FORMAT), client)
                        nicknames.append(name)
                    else:
                        # if just a simple message is sent, then it is broadcasted to all the clients
                        server.sendto(
                            f"[{nicknames[index]}]: {message.decode(FORMAT)}".encode(FORMAT), client)

                        if message.decode(FORMAT) == "exit":
                            raise ConnectionResetError
            except ConnectionResetError:
                exitName = nicknames[clients.index(client)]
                # if the client exits then the client is removed in the list and then
                print(
                    f"{exitName} has lost connection!")
                clients.remove(client)
                nicknames.remove(exitName)

                # we use this function to send to the rest of the clients that the client with the curr name left
                handle_disconnect(exitName)
        # NOTE: The CLIENTS LIST includes TUPLES of the ADDRESS and PORT of each client!


# making a thread to the receive function so that it keeps "listening" for messages
t1 = threading.Thread(target=receive)
# making a thread to the broadcast function so that it constantly waits for messages to be added
t2 = threading.Thread(target=broadcast)
# to the message queue, so that it will take them and print them to all the clients that are
# stored inside the clients list

t1.start()
t2.start()
