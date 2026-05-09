import socket
import json

HOST = "127.0.0.1"
PORT = 8080 #proxy server we are sending to

data = {
    "server_ip": "127.0.0.1",
    "server_port": 7001,
    "message": "ping"
}

json_data = json.dumps(data) #Python dict → JSON string → UTF-8 bytes → TCP stream
byte_data = json_data.encode("utf-8")

for i in range(5):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create NEW socket each time
    client.connect((HOST, PORT))
    
    client.sendall(byte_data)
    
    response = client.recv(1024)
    
    print(f"{response.decode()}")
    
    client.close()  # Close after each request
'''
Sending python data structure over TCP connection: Python dict → JSON string → UTF-8 bytes → TCP stream
'''