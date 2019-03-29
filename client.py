from socket import *
import sys
import time

server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

host_port = "%s:%s" % (server_host, server_port)

try:

    # start time
    init_time = time.time()

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host,int(server_port)))
    client_socket.settimeout(60)

    header = {
        "first_header" : "GET /%s HTTP/1.1" %(filename),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": host_port,
    }
    http_header = "\r\n".join("%s:%s" % (item, header[item]) for item in header)

    client_socket.sendall(http_header.encode())

except IOError:
    sys.exit(1)

response_message = client_socket.recv(1024).decode()

# end time
end_time = time.time()

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

client_socket.close()

print('Response message:\n', response_message)

