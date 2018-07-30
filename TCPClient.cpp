//
// Created by nate on 5/14/18.
//

#include "TCPClient.h"
#include <errno.h>
#include <stdio.h>
#include <iostream>

unsigned int TCPClient::bytes_ready_to_send() {
  return send_buf_offset;
}

unsigned int TCPClient::bytes_ready_to_recv() {
  return recv_buf_offset;
}

int TCPClient::get_fd() {
  return socket_fd;
}

bool TCPClient::add_send_data(char *data, unsigned int data_len) {
  // Don't add more data into send buffer if it's full (or would overflow)
  if (data_len > send_buf_offset + DEFAULT_BUFFER_SIZE) {
    return false;
  } else {
    memcpy(&send_buffer[send_buf_offset], data, data_len);
    send_buf_offset += data_len;
    return true;
  }
}

bool TCPClient::get_recv_data(char *buf, unsigned int buf_len) {
  // Ensure the receive buffer is big enough to hold the data we're getting
  if (buf_len < recv_buf_offset)
    return false;
  else {
    memcpy(buf, recv_buffer, recv_buf_offset);
    return true;
  }
}

const char *TCPClient::get_printable_address() {
  // Buffer will be big enough for either a v4 or v6 address
  // AND big enough to put :65535 (the port) at the end.
  static char print_buf[NI_MAXHOST + NI_MAXSERV];
  static char host_buf[NI_MAXHOST];
  static char port_buf[NI_MAXSERV];

  int ret;
  // Verify address family is either v4 or v6
  switch (client_addr.ss_family) {
    case AF_INET:
      break;
    case AF_INET6:
      break;
    default:
      return nullptr;
  }

  // If we get here, we're good to go!
  ret = getnameinfo((struct sockaddr *)&client_addr, client_addr_len,
                    host_buf, NI_MAXHOST,
                    port_buf, NI_MAXSERV, NI_NUMERICHOST | NI_NUMERICSERV);
  if (ret != 0) {
    std::cout << "getnameinfo error " << gai_strerror(errno) << std::endl;
    return nullptr;
  }

  strncpy(print_buf, host_buf, NI_MAXHOST);
  print_buf[strlen(host_buf)] = ':';
  strncpy(&print_buf[strlen(host_buf) + 1], port_buf, NI_MAXSERV);

  return print_buf;
}
