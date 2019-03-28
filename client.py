from socket import *
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = sys.argv[2]
filename = sys.argv[3]

try:
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((SERVER_HOST,SERVER_PORT))

    header = {
        "first header: ": "GET /%s HTTP/1.1" % filename,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": SERVER_HOST + ':' + SERVER_PORT,
    }

    headers = ''

    for item in header:
        headers += item + ':' + header[item] + '\r\n'

    clientSocket.sendall(headers)

except IOError:
    sys.exit(1)
