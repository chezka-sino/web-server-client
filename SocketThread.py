"""SocketThread.py: Socket thread class"""
__author__ = "Chezka Sino (ID: 9028-67538)"

import threading


class SocketThread(threading.Thread):
    """
    This is a class for a connection socket thread

    Attributes:
        conn (socket): Connection socket
        addr (tuple): address of the socket
    """

    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.connectionSocket = conn
        self.address = addr
        self.connectionSocket.settimeout(10.0)

    def run(self):
        while True:
            try:
                message = self.connectionSocket.recv(1024).decode()
                print(message)

                headers = message.split('\n')
                filename = headers[0].split()[1]

                file = open(filename[1:])
                outputdata = file.read()
                file.close()

                # Sends the content of the header and content of the requested file to the client
                response = 'HTTP/1.1 200 OK \n\n' + outputdata
                self.connectionSocket.sendall(response.encode())

            except IOError:
                # Sends response message for file not found
                response = 'HTTP/1.1 404 Not Found\n\n404 File Not Found'
                self.connectionSocket.sendall(response.encode())
