from socket import *

# sources
# Web server -- http://joaoventura.net/blog/2017/python-webserver/
# RTT calculate == https://www.geeksforgeeks.org/program-calculate-round-trip-time-rtt/

serverPort = 8000
serverHost = '0.0.0.0'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print("Listening on  port %s ..." % serverPort)

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()

    try:
        # Get the client request
        message = connectionSocket.recv(1024).decode()
        print(message)

        # Parse HTTP headers
        filename = message.split()[1]
        file = open(filename[1:])

        outputdata = file.read()
        file.close()

        response = 'HTTP/1.1 200 OK\n\n' + outputdata


    except IOError:
        errorFile = open('404.html')
        errorOutput = errorFile.read()
        response = 'HTTP/1.1 404 NOT FOUND\n\n' + errorOutput

    connectionSocket.sendall(response.encode())
    connectionSocket.close()

serverSocket.close()