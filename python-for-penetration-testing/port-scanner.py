#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Please enter the IP: ")
port = int(input("Please enter the port: "))


def portScanner(port):
    s.settimeout(5)
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")


portScanner(port)
