#!/usr/bin/python3

import sys
from socket import socket, SOCK_DGRAM, AF_INET

def print_error(e, f="UNKNOWN"):
    print("Error in %s!" % (f))
    print(e)
    print(type(e))

def send_data(udp_sock, endpoint, data):
  try:
    ret = udp_sock.sendto(bytes(data, 'utf-8'), endpoint)
    print("Sent %d bytes" % (ret))
  except Exception as e:
    print_error(e, "sendto")

def main():
  print(len(sys.argv))
  if len(sys.argv) >= 3:
    ip = sys.argv[1]
    try:
      port = int(sys.argv[2])
    except:
      print("Port %s unable to be converted to number, run with HOST PORT" % (sys.argv[2]))
      sys.exit(1)
  data = None
  if len(sys.argv) == 4:
    data = sys.argv[3]
    print("Will send %s to %s:%d via udp" % (data, ip, port))

  if data == None:
    data = input("Enter data to send: ")

  try:
    udp_sock = socket(AF_INET, SOCK_DGRAM)
    send_data(udp_sock, (ip, port), data)
  except Exception as e:
    print_error(e, "socket")

if __name__ == "__main__":
  main()
