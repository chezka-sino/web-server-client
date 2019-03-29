from socket import *
from SocketThread import SocketThread

# sources
# Web server -- http://joaoventura.net/blog/2017/python-webserver/
# RTT calculate == https://www.geeksforgeeks.org/program-calculate-round-trip-time-rtt/

if __name__ == '__main__':

    serverPort = 8000
    serverHost = '0.0.0.0'
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen()
    threads = []

    while True:
        # Establish the connection
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()

        socketThread = SocketThread(connectionSocket,addr)
        socketThread.setDaemon(True)
        socketThread.start()

        hostname, aliases, addresses = gethostbyaddr(gethostbyname(gethostname()))
        print('|==========================================================')
        print('| Computer Name:     ', gethostname())
        print('| Hostname:          ', hostname)
        print('| Aliases:           ', aliases)
        print('| Addresses:         ', addresses)
        print('| Socket Family:     ', connectionSocket.family)
        print('| Socket Type:       ', connectionSocket.type)
        print('| Protocol:          ', connectionSocket.proto)
        print('| Timeout:           ', connectionSocket.gettimeout())
        print('| Peer name:         ', connectionSocket.getpeername())
        print('|==========================================================\n')

        threads.append(socketThread)

    serverSocket.close()