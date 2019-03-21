#import socket module
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
# TODO Prepare a server socket
#Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr =  serverSocket.accept()

    try:
        # TODO check message
        message = connectionSocket.recv(1024)

        # TODO uncomment after filling out message
        # filename = message.split()[1]
        #f = open(filename[1:]

        # TODO outputdata
        #outputdata = #Fill in start #Fill in end

        # TODO Send one HTTP header line into socket
        #Fill in start
        #Fill in end

        # TODO uncomment after filling out outputdata
        # Send the content of the requested file to the client
        #for i in range(0, len(outputdata)):
        #    connectionSocket.send(outputdata[i])
        #connectionSocket.close()
    except IOError:
        print("placeholder")
        # TODO Send response message for file not found
        #Fill in start
        #Fill in end
        # TODO Close client socket
        #Fill in start
        #Fill in end

serverSocket.close()