#!/usr/bin/python3

import sys
from socket import socket, SOCK_STREAM, AF_INET

def print_error(e, f="UNKNOWN"):
    print("Error in %s!" % (f))
    print(e)
    print(type(e))

def send_data(tcp_sock, data):
  try:
    ret = tcp_sock.send(bytes(data, 'utf-8'))
    print("Sent %d bytes" % (ret))
  except Exception as e:
    print_error(e, "send")

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
    print("Will send %s to %s:%d via tcp" % (data, ip, port))

  if data == None:
    data = input("Enter data to send: ")

  try:
    tcp_sock = socket(AF_INET, SOCK_STREAM)
  except Exception as e:
    print_error(e, "socket")
  
  try:
    tcp_sock.connect((ip, port))
  except Exception as e:
    print_error(e, "connect")
  
  try:
    send_data(tcp_sock, data)
  except Exception as e:
    print_error(e, "send_data")

if __name__ == "__main__":
  main()
