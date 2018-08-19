#!/usr/bin/python3

import sys
from socket import socket, SOCK_STREAM, AF_INET
from select import select
import traceback
from threading import Thread

class TCPServer:
  def __init__(self):
    self.client_threads = []

  def add_client(self, client):
    self.client_threads.append(client)

  def send_message(self, client, message):
    print(message)
    for client_thread in self.client_threads:
      if client != client_thread:
        client_thread.queue_message(message)

class TCPClient(Thread):
  def __init__(self, client_sock, client_address, server):
    # Call parent (thread) constructor
    super(TCPClient, self).__init__()
    self.client_sock = client_sock
    self.client_address = client_address
    self.keep_running = True
    self.read_fds = [self.client_sock]
    self.write_fds = [self.client_sock]
    self.pending_messages = []
    self.server = server
    self.nick = "%s:%d" % (self.client_address[0], self.client_address[1])
    self.server.send_message(self, "%s joined the chat" % (self.nick))

  def run(self):
    while self.keep_running == True:
      try:
        if len(self.pending_messages) > 0:
          readlist, writelist, _ = select(self.read_fds, self.write_fds, [], .1)
        else:
          readlist, writelist, _ = select(self.read_fds, [], [], .1)
        if self.client_sock in readlist:
          data = self.client_sock.recv(4096)
          if len(data) == 0:
            self.keep_running = False
            self.client_sock.close()
            self.server.send_message(self, "%s left the chat" % (self.nick))
            continue
          data_str = data.decode('utf-8')
          if data_str.startswith('nick:'):
            _, nick = data_str.split(':')
            print("Got nick %s" % (nick))
            self.nick = nick
            self.server.send_message(self, "%s:%d changed nickname to %s" % (self.client_address[0], self.client_address[1], self.nick))
          else:
            self.server.send_message(self, "%s said: %s" % (self.nick, data_str))
		

        if self.client_sock in writelist and len(self.pending_messages) > 0:
          for message in self.pending_messages:
            try:
              self.client_sock.send(bytes(message, 'utf-8'))
            except Exception as e:
              self.client_sock.close()
              self.keep_running = False
          self.pending_messages = []
      except Exception:
        self.keep_running = False

    print("Shutting down client socket.")
    self.client_sock.close()

  def queue_message(self, message):
    self.pending_messages.append(message)

  def stop(self):
    print("Stopping.")
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

  my_server = TCPServer()

  while (quit == False):
    try:
      readlist, writelist, exceptlist = select(read_sockets, write_sockets, except_sockets, .1)
    except KeyboardInterrupt as k:
      quit = True
    except Exception as e:
      print_error(e, "select")

    if server_sock in readlist:
      try:
        client_sock, (client_ip, client_port) = server_sock.accept()
        temp_client_thread = TCPClient(client_sock, (client_ip, client_port), my_server)
        #client_threads.append(temp_client_thread)
        my_server.add_client(temp_client_thread)
        temp_client_thread.start()
      except KeyboardInterrupt as k:
        quit = True
      except Exception as e:
        print_error(e, "accept")

    for client_thread in my_server.client_threads:
      if client_thread.keep_running == False:
        print("Removing client thread.")
        client_thread.join()
        my_server.client_threads.remove(client_thread)
        break

  try:
    print("Closing sockets, have %d clients." % len(my_server.client_threads))
    for client_thread in my_server.client_threads:
      print("Stopping client thread?")
      client_thread.stop()
      client_thread.join()

    server_sock.close(2)

  except:
    pass
if __name__ == "__main__":
  main()
