"""client.py: Single threaded Web Client"""
__author__ = "Chezka Sino (ID: 9028-67538)"

from socket import *
import sys
import time

SERVER_HOST = sys.argv[1]
SERVER_PORT = sys.argv[2]
filename = sys.argv[3]

host_port = "%s:%s" % (SERVER_HOST, SERVER_PORT)

try:

    # start time for calculating RTT
    init_time = time.time()

    # Prepare a client socket
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER_HOST, int(SERVER_PORT)))
    client_socket.settimeout(60)

    request = ""
    request += "GET /%s HTTP/1.1" % filename
    request += "Host:%s:%s" % (SERVER_HOST, SERVER_PORT)

    # Send the GET request to server
    client_socket.sendall(request.encode())

except IOError:
    sys.exit(1)

# Response message from the server
response_message = client_socket.recv(1024).decode()

# end time for calculating RTT
end_time = time.time()

# This gets the necessary server details
print('|==========================================================')
hostname, aliases, addresses = gethostbyaddr(gethostbyname(gethostname()))
print('| Hostname:          ', hostname)
print('| Aliases:           ', aliases)
print('| Addresses:         ', addresses)
print('| Socket Family:     ', client_socket.family)
print('| Socket Type:       ', client_socket.type)
print('| Protocol:          ', client_socket.proto)
print('| Timeout:           ', client_socket.gettimeout())
print('| Peer name:         ', client_socket.getpeername())
print('| RTT:               ', '{0:.2f}'.format(abs(init_time - end_time) * 1000) + 'ms')
print('|==========================================================\n')

# Close client socket after one request
client_socket.close()

# Shows the response message from the server
print('Response message:\n', response_message)

