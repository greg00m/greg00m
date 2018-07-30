/**
 * In-class demonstrated UDP server example. 04-09-2018
 */

#include <iostream>
#include <sys/socket.h>
#include <errno.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

/**
 *
 * Simple UDP server example. Reads in IP PORT
 * from the command line, and receives via UDP to IP:PORT.
 *
 * e.g., ./udpserver 127.0.0.1 8888
 *
 * @param argc count of arguments on the command line
 * @param argv array of command line arguments
 * @return 0 on success, non-zero if an error occurred
 */
int main(int argc, char *argv[]) {
  // Alias for argv[1] for convenience
  char *ip_string;
  // Alias for argv[2] for convenience
  char *port_string;

  unsigned int port;
  // The socket used to send UDP data on
  int udp_socket;
  // Variable used to check return codes from various functions
  int ret;
  // IPv4 structure representing and IP address and port of the destination
  struct sockaddr_in recv_addr;

  // Variable to hold address of client that sent data
  struct sockaddr_in client_address;
  // Length of the client address of client
  socklen_t client_address_length;
  // Buffer to hold data received from network
  char recv_buf[2048];

  // Set dest_addr to all zeroes, just to make sure it's not filled with junk
  // Note we could also make it a static variable, which will be zeroed before execution
  memset(&recv_addr, 0, sizeof(struct sockaddr_in));

  // Note: this needs to be 3, because the program name counts as an argument!
  if (argc < 3) {
    std::cerr << "Please specify IP PORT as first two arguments." << std::endl;
    return 1;
  }
  // Set up variables "aliases"
  ip_string = argv[1];
  port_string = argv[2];

  // Create the UDP socket.
  // AF_INET is the address family used for IPv4 addresses
  // SOCK_DGRAM indicates creation of a UDP socket
  udp_socket = socket(AF_INET, SOCK_DGRAM, 0);

  // Make sure socket was created successfully, or exit.
  if (udp_socket == -1) {
    std::cerr << "Failed to create udp socket!" << std::endl;
    std::cerr << strerror(errno) << std::endl;
    return 1;
  }

  // inet_pton converts an ip address string (e.g., 1.2.3.4) into the 4 byte
  // equivalent required for using the address in code.
  // Note that because dest_addr is a sockaddr_in (again, IPv4) the 'sin_addr'
  // member of the struct is used for the IP
  ret = inet_pton(AF_INET, ip_string, (void *)&recv_addr.sin_addr);

  // Check whether the specified IP was parsed properly. If not, exit.
  if (ret == -1) {
    std::cerr << "Failed to parse IPv4 address!" << std::endl;
    std::cerr << strerror(errno) << std::endl;
    close(udp_socket);
    return 1;
  }

  // Convert the port string into an unsigned integer.
  ret = sscanf(port_string, "%u", &port);
  // sscanf is called with one argument to convert, so the result should be 1
  // If not, exit.
  if (ret != 1) {
    std::cerr << "Failed to parse port!" << std::endl;
    std::cerr << strerror(errno) << std::endl;
    close(udp_socket);
    return 1;
  }

  // Set the address family to AF_INET (IPv4)
  recv_addr.sin_family = AF_INET;
  // Set the destination port. Use htons (host to network short)
  // to ensure that the port is in big endian format
  recv_addr.sin_port = htons(port);

  // Bind tells the system to open the IP:PORT for receiving data,
  // and to send any data received to this socket.
  ret = bind(udp_socket, (struct sockaddr *)&recv_addr, sizeof(struct sockaddr_in));

  // Check if bind worked, clean up and exit if not.
  if (ret == -1) {
    std::cerr << "Failed to bind!" << std::endl;
    std::cerr << strerror(errno) << std::endl;
    close(udp_socket);
    return 1;
  }

  // Recv gets the data, but not who sent it!
  //ret = recv(udp_socket, recv_buf, 2047, 0);

  // Set client_address_length, so recvfrom knows how big a buffer is available
  client_address_length = sizeof(struct sockaddr_in);
  std::cout << "Client address length (of ipv4 address) is " << client_address_length << std::endl;

  // Receive data using recvfrom. client_address will hold the client
  // address that sent the data.
  ret =
    recvfrom(udp_socket, recv_buf, 2047, 0,
             (struct sockaddr *)&client_address, &client_address_length);

  if (ret == -1) {
    std::cerr << "Failed to recv!" << std::endl;
    std::cerr << strerror(errno) << std::endl;
    close(udp_socket);
    return 1;
  }
  std::cout << "Received " << ret << " bytes from client with address length "
            << client_address_length << "\n";
  recv_buf[ret] = '\0';

  std::cout << "Received data: " << recv_buf << std::endl;


  close(udp_socket);
  return 0;
}

