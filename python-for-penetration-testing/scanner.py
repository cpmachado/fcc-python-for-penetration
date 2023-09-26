#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<------------------------------------------------------------------->")

ip_addr = input("Please enter the IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input(
    """\nPlease enter the type of scan you want to run
                  1) SYN ACK scan
                  2) UDP scan
                  3) Comprehensive scan\n"""
)

print("You have selected option: ", resp)

if resp == "1":
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", "-v -sS")
    print(scanner.scaninfo())

    target = scanner[ip_addr]
    print("IP Status: ", target.state)
    print(target.all_protocols())
    print("Open Ports: ", target["tcp"].keys())
elif resp == "2":
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", "-v -sU")
    print(scanner.scaninfo())

    target = scanner[ip_addr]
    print("IP Status: ", target.state)
    print(target.all_protocols())
    print("Open Ports: ", target["udp"].keys())
elif resp == "3":
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", "-v -sS -sV -sC -A -O")
    print(scanner.scaninfo())

    target = scanner[ip_addr]
    print("IP Status: ", target.state)
    print(target.all_protocols())
    print("Open Ports: ", target["tcp"].keys())
elif resp >= "4":
    print("Please enter a valid option")
