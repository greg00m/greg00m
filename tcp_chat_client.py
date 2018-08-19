#!/usr/bin/python3

import sys
from socket import socket, SOCK_STREAM, AF_INET
from select import select

def print_error(e, f="UNKNOWN"):
    print("Error in %s!" % (f))
    print(e)
    print(type(e))

def send_data(tcp_sock, data):
  try:
    ret = tcp_sock.send(bytes(data, 'utf-8'))
  except KeyboardInterrupt as k:
    raise KeyboardInterrupt()
  except Exception as e:
    print_error(e, "send")

def recv_data(tcp_sock):
  try:
    data = tcp_sock.recv(4096)
    if len(data) == 0:
      return False
    print(data.decode('utf-8'))
    return True
  except Exception as e:
    print_error(e, "recv")

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

  try:
    tcp_sock = socket(AF_INET, SOCK_STREAM)
  except Exception as e:
    print_error(e, "socket")
  
  try:
    tcp_sock.connect((ip, port))

    print("Connect succeeded.")
  except Exception as e:
    print_error(e, "connect")

  tcp_sock.setblocking(0)
  read_sockets = [tcp_sock, sys.stdin]
  
  try:
    while data != 'quit':
      readlist, writelist, _ = select(read_sockets, [], [], .1)
      try:
        if tcp_sock in readlist:
          if recv_data(tcp_sock) == False:
            print("Server went away, shutting down.")
            data = 'quit'

        if sys.stdin in readlist:
          data = sys.stdin.readline().strip()
          if data != 'quit':
            send_data(tcp_sock, data)
          else:
            print("Got client quit.")
      except KeyboardInterrupt as e:
        data = 'quit'
        print("Got keyboard kill")

  except Exception as e:
    print_error(e, "send_data")

  finally:
    tcp_sock.close()

if __name__ == "__main__":
  main()
