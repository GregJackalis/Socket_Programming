import socket
import threading


# USING CAPS FOR THESE VARIABLES BECAUSE THEY ARE CONSTANTS

# this is basically a "bytes-standard", meaning a fixed number of bytes the server can receive through the client's message
HEADER = 64

# need to look more info about PORTS
PORT = 5050

# SERVER = "192.168.1.16"  # this makes it so that it runs on this device in my local network
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)  # it actually gets our local ipv4 address

ADDR = (SERVER, PORT)  # needs to be in a tuple
FORMAT = 'utf-8'

# this is the message that is returned to the server when the client leaves the connection, it is used to notify the server
# that the client left and that it can close the connection and disconnect the client from the server
DISCONNECT_MESSAGE = "!DISCONNECT"


# MAKING A SOKCET TO OPEN CONNECTIVITY TO CLIENTS
# this is how we make a new socket, and the argument basically says what type of ip
# address is the socket going to accept or wait for
# INET6 is for ipv6, SOCK_STREAM means that the socket is streaming
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# keep in mind that the .AF_INET is basically about categorizing (which family does the socket belong to?)
# and the .SOCK_STREAM is the "type of socket"

# this means that the socket has been bounded to the ADDR address
server.bind(ADDR)


def handle_client(conn, addr):
    print("[NEW CONNECTION] {} CONNECTED".format(addr))

    connected = True
    while connected:
        # this tells how long is the message that is coming
        msg_length = conn.recv(HEADER).decode(FORMAT)

        # if a message is returned (which when the server is started there is on connection without a msg, so this if helps the script not crash)
        if msg_length:
            # here the length is turned into an integer
            msg_length = int(msg_length)
            # and then the length is  seud in here so that the server knows how many bytes it will be expecting for the actual message
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

            # In order now for the server to send back a message:
            conn.send("Message received!".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print("[LISTENING] Server is listening on {}".format(SERVER))
    while True:
        conn, addr = server.accept()

        # when a new connection occurs, we pass that connection and the address to the handle client function
        # Threading is used when we want to handle more than one client at a time
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread = thread.start()
        print(f"\n[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] Server is starting...")
start()
