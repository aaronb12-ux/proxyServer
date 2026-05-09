import socket
import json
HOST = "127.0.0.1"
PORT = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

while True:

    conn, addr = server.accept() #accept data from the proxy

    data = conn.recv(4096)

    conn.sendall(b"pong")

    conn.close()


