"""servey.py: Multithreaded Web Server"""
__author__ = "Chezka Sino (ID: 9028-67538)"

from socket import *

# Imports the thread class for sockets for multithreading
from SocketThread import SocketThread

if __name__ == '__main__':

    # Prepare a server socket
    serverPort = 8000
    serverHost = '0.0.0.0'
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(5)
    threads = []

    while True:
        # Establish the connection
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()

        # Initialized a thread for the connection socket
        socketThread = SocketThread(connectionSocket,addr)
        socketThread.setDaemon(True)
        socketThread.start()

        # This gets the necessary server details
        hostname, aliases, addresses = gethostbyaddr(gethostbyname(gethostname()))
        print('|==========================================================')
        print('| Computer Name:     ', gethostname())
        print('| Hostname:          ', hostname)
        print('| Aliases:           ', aliases)
        print('| Addresses:         ', addresses)
        print('| Socket Family:     ', connectionSocket.family)
        print('| Socket Type:       ', connectionSocket.type)
        print('| Protocol:          ', connectionSocket.proto) # TODO protocol name?
        print('| Timeout:           ', connectionSocket.gettimeout())
        print('| Peer name:         ', connectionSocket.getpeername())
        print('|==========================================================\n')

        threads.append(socketThread)
        connectionSocket.close()

    serverSocket.close()