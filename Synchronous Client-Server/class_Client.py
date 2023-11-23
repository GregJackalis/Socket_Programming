import socket

class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.FORMAT = 'utf-8'

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
            clientSocket.connect((self.HOST, self.PORT))
            print(clientSocket.recv(1024).decode(self.FORMAT))

            msg = input()
            if msg == "exit":
                clientSocket.send("[CLIENT] Client has been disconnected".encode(self.FORMAT))
                clientSocket.close()
            else:
                clientSocket.send(f"{msg}".encode(self.FORMAT))



client = Client(socket.gethostbyname(socket.gethostname()), 50930)
client.run()