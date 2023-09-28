#!/usr/bin/python3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4000


server.bind((host, port))

server.listen(3)

print(f"listening on {host}:{port}")

while True:
    client, addr = server.accept()
    print("received connection from %r" % str(addr))
    message = "hello! Thank you for connecting to the server\r\n"
    client.send(message.encode("ascii"))
    client.close()
