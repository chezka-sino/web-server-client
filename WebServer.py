from socket import *

# sources
# Web server -- http://joaoventura.net/blog/2017/python-webserver/
# RTT calculate == https://www.geeksforgeeks.org/program-calculate-round-trip-time-rtt/

serverPort = 8000
serverHost = '0.0.0.0'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        print(message)

        # Parse HTTP headers
        filename = message.split()[1]
        file = open(filename[1:])

        outputdata = file.read()
        file.close()

        connectionSocket.send('HTTP/1.1 200 OK\n\n')

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        connectionSocket.send('ERROR 404: File Not Found')
        connectionSocket.close()

serverSocket.close()