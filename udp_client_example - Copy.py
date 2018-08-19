#!/usr/bin/python3

import sys
from socket import socket, AF_INET, SOCK_DGRAM

ip = sys.argv[1]
port = int(sys.argv[2])
data = sys.argv[3]
udp_sock = socket(AF_INET, SOCK_DGRAM)
ret = udp_sock.sendto(bytes(data, 'utf-8'),(ip, port))
print("Sent %d bytes to %s:%d" % (ret, ip, port))


