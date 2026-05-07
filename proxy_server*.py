import socket
import json
HOST = "127.0.0.1"
PORT = 8080

blockList = {"192.168.1.1"}

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.bind((HOST, PORT))
proxy.listen()

conn, addr = proxy.accept()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = conn.recv(4096)
json_str = data.decode("utf-8")
payload = json.loads(json_str)

server.connect((payload["server_ip"], payload["server_port"]))


if payload["server_ip"] in blockList: #return error to client
    print("yooooo")
    conn.sendall(b"Error")
    conn.close()
    proxy.close()
    server.close()
    exit()

else:
   
    server.sendall(data)

    response = server.recv(4096)

    conn.sendall(response)


'''
Client sends a JSON payload over TCP to the proxy server. THe proxy then pings the server. The server then pongs back to the proxy, and
then the proxy pongs back to the client

This proxy must PARSE the JSOn payload sent from the client and extract the: server_ip, server_port, and message

Check if server_ip is in the IP blocklist

If that IP is blocked, reply with 'Error' and do not forward the request to the server

'''
