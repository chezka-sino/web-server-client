from socket import *
import sys
import time

server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

# start time
init_time = time.time()

host_port = "%s:%s" %(server_host, server_port)

try:
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect((server_host,int(server_port)))
    header = {
        "first_header" : "GET /%s HTTP/1.1" %(filename),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": host_port,
    }
    http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
    print(http_header)

    client_socket.send(http_header.encode())

except IOError:
    sys.exit(1)

response_message = client_socket.recv(1024).decode()

client_socket.close()
print(response_message)

print('========================\n')
print('TEST OUTPUT')
print('host name?', gethostbyname())
print('socket family?', socket.getaddrinfo())


# end time
end_time = time.time()
print('\nRTT:', '{0:.2f}'.format(abs(init_time - end_time) * 1000) + 'ms')