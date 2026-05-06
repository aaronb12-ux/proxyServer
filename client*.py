import socket
import json
#send JSON payload to the proxy server
HOST = "127.0.0.1"
PORT = 8080 #proxy server we are sending to

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = {
    "server_ip": "192.168.1.1",
    "server_port": 7000,
    "message": "ping"
}

client.connect((HOST, PORT))

json_data = json.dumps(data) #Python dict → JSON string → UTF-8 bytes → TCP stream

byte_data = json_data.encode("utf-8")

client.sendall(byte_data)

data, addr = client.recvfrom(1024)

print(f"We received the message: {data.decode()}")


'''
Sending python data structure over TCP connection: Python dict → JSON string → UTF-8 bytes → TCP stream
'''