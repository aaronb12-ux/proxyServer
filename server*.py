import socket
import json
HOST = "127.0.0.1"
PORT = 7000



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()



conn, addr = server.accept() #accept data from the server

data = conn.recv(4096)
json_str = data.decode("utf-8")
payload = json.loads(json_str)



