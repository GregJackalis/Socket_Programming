from class_Server import Server
import socket

server = Server(socket.gethostbyname(socket.gethostname()), 50930)
server.run()