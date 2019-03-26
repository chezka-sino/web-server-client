from socket import *
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = sys.argv[2]
filename = sys.argv[3]

try:
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((SERVER_HOST,SERVER_PORT))



except IOError:
    sys.exit()