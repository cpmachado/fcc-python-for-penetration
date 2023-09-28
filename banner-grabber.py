#!/usr/bin/python3

import socket


def banner(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    print(str(s.recv(1024)))


def main():
    ip = input("Please enter the IP: ")
    port = input("Please enter the port: ")
    banner(ip, int(port))


main()
