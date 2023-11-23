import socket

class Server:
    def __init__(self, host, port):
        # making and assigning two variables, host and port
        self.HOST = host
        self.PORT = port
        self.FORMAT = 'utf-8'

    def run(self):
        # This function will contain:
            # 1) The socket binding to IP Address and PORT (in a tuple)
            # 2) Set socket to listen for connections
            # 3) Client connection, using the .accept() method
            # 4) Use a loop, so that while the socket is connected to client and it's "alive", 
            #   it will wait for messages/requests
            # 5) Process data and respond

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            # 1)
            serverSocket.bind((self.HOST, self.PORT))

            # this is a method called "set-socket_options", these options are used to configure the behaviour of a socket
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # the SOL_SOCKET represents the laeyer of the socket, It's used as the level argument in setsockopt to 
            # indicate that the option being set is at the socket level


            # 2)
            serverSocket.listen()
            print("Server is listening...")
            # 3)
            comm_Sock, address = serverSocket.accept()

            # 4) ==> Now, using the "with" block we basically say that we won't accept any other connection
            #        until this with block breaks (it works like a while loop)
            with comm_Sock:
                print(f"[CLIENT] Client from {address} address has been connected!")
                comm_Sock.send(f"[SERVER] You have succesfully connected to the server at port {self.PORT}".encode(self.FORMAT))


                # with comm_Sock being true, so being connected, then wait for a message
                while True:
                    msg = comm_Sock.recv(1024).decode(self.FORMAT)

                    print(f"[CLIENT {address}] Says: {msg}")

                    if not msg:
                        break

                    # 5)
                    comm_Sock.sendall(msg.encode(self.FORMAT))

