import atexit
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = "192.168.1.16"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_to_server(msg):
    # encoding the message string into a bytes-like object
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # b means the bytes representation of this
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    print(client.recv(HEADER).decode(FORMAT))


send_to_server("Hello World!")
input()  # this is used so that every sentence is printed after the "client" presses enter
send_to_server("Hello Server! ")
input()
send_to_server("I'm connected to the server!")
input()
send_to_server("Woooooo")

print("\nInput your own sentence to send to the server: ")
send_to_server(input())

# Now with this message right here, when I re-run through the laptop's terminal this script, I will reconnect and re-print
# all the messages above with the only difference that the [ACTIVE CONNECTIONS] will still remain 1
# (because I exited and reconnected basically)
send_to_server(DISCONNECT_MESSAGE)

# Reminder that by opening another terminal through the laptop, I can have more than one client running in "real-time"


# SMALL DETAIL
# In case the client press control+C or closes the terminal, I want to return the disconnect message to the server
# In order to do that, I need to use two libraries: signal and sys

# HAVEN'T FOUND A SOLUTION YET

# def signal_handler(signum):
#     disconnect_sent = False
#     if signum == signal.SIGINT or signum == signal.SIGHUP:
#         if not disconnect_sent:
#             send_to_server(DISCONNECT_MESSAGE)
#             disconnect_sent = True
#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGHUP, signal_handler)

# def disconnect():
#     send_to_server(DISCONNECT_MESSAGE)
#     client.close()


# atexit.register(disconnect)
