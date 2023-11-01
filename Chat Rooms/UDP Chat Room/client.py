import socket
import threading
import random

FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((socket.gethostbyname(socket.gethostname()), random.randint(8000, 9000))) 
# NOTE: Pay attention how we are NOT using .connect like we do in TCP where we connect to the same address and port with the Server Socket
# but instead we bind the client socket just like we do with the server. Then because we need to bind it to the same address of course
# but different port number, we can just use the random library and generate a random number between 8000 and 9000


def receive():
    while True:
        try:
            message, address = client.recvfrom(1024)  # here we don't care about the address of the server- we just want the message sent to us
            print(message.decode(FORMAT))
        except: 
            pass


def sending():
    while True:
        message = input("")
        if message == 'q':
            client.sendto("exit".encode(FORMAT), (socket.gethostbyname(socket.gethostname()), 9095))
            exit()
        else:
            client.sendto(message.encode(FORMAT), (socket.gethostbyname(socket.gethostname()), 9095))


client.sendto(f'Nickname: {input("Enter a nickname: ")}'.encode(FORMAT), (socket.gethostbyname(socket.gethostname()), 9095))
t = threading.Thread(target=receive)
t.start()
sending()
