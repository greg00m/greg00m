#!/usr/bin/python3

import sys
from socket import socket, SOCK_STREAM, AF_INET
from select import select
import traceback
from threading import Thread



class TCPClient(Thread):
  def __init__(self, client_sock, client_address):
    # Call parent (thread) constructor
    super(TCPClient, self).__init__()
    self.client_sock = client_sock
    self.client_address = client_address
    self.keep_running = True
    self.read_fds = [self.client_sock]

  def run(self):
    while self.keep_running == True:
      try:
        readlist, _, _ = select(self.read_fds, [], [])
        if self.client_sock in readlist:
          data = self.client_sock.recv(4096)
          self.client_sock.send(data)
          if len(data) == 0:
            self.client_sock.close()
      except Exception:
        self.keep_running = False

    print("Shutting down client socket.")
    self.client_sock.close()

  def stop(self):
    self.keep_running = False

def print_error(e, f="UNKNOWN"):
    print("Error in %s!" % (f))
    print(e)
    print(type(e))
    traceback.print_exc()

def main():
  if len(sys.argv) == 3:
    ip = sys.argv[1]
    try:
      port = int(sys.argv[2])
    except:
      print("Port %s unable to be converted to number, run with HOST PORT" % (sys.argv[2]))
      sys.exit(1)
  else:
    print("Run with %s HOST PORT" % (sys.argv[0]))
    sys.exit(1)

  try:
    server_sock = socket(AF_INET, SOCK_STREAM)
  except Exception as e:
    print_error(e, "socket")
    sys.exit(1)
  
  try:
    server_sock.bind((ip, port))
  except Exception as e:
    print_error(e, "bind")
    sys.exit(1)

  try:
    server_sock.listen(100)
  except Exception as e:
    print_error(e, "listen")
    sys.exit(1)

  read_sockets = []
  write_sockets = []
  except_sockets = []
  client_threads = []

  read_sockets.append(server_sock)
  except_sockets.append(server_sock)
  quit = False

  readlist, writelist, exceptlist = [], [], []

  while (quit == False):
    try:
      readlist, writelist, exceptlist = select(read_sockets, write_sockets, except_sockets, 3)
    except KeyboardInterrupt as k:
      quit = True
    except Exception as e:
      print_error(e, "select")

    if server_sock in readlist:
      try:
        client_sock, (client_ip, client_port) = server_sock.accept()
        temp_client_thread = TCPClient(client_sock, (client_ip, client_port))
        client_threads.append(temp_client_thread)
        temp_client_thread.start()
      except KeyboardInterrupt as k:
        quit = True
      except Exception as e:
        print_error(e, "accept")

    for client_thread in client_threads:
      if client_thread.keep_running == False:
        print("Removing client thread.")
        client_thread.join()
        client_threads.remove(client_thread)
        break;

  try:
    print("Closing sockets.")
    server_sock.close()
    for client_thread in client_threads:
      client_thread.stop()
      client_thread.join()
  except:
    pass
if __name__ == "__main__":
  main()
