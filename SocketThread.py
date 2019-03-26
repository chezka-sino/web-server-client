import threading
import time


class SocketThread(threading.Thread):

    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.connectionSocket = conn
        self.address = addr
        self.running = True

    def run(self):
        while self.running:
            try:
                message = self.connectionSocket.recv(1024).decode()
                print(message)

                headers = message.split('\n')
                filename = headers[0].split()[1]

                file = open(filename[1:])
                outputdata = file.read()
                file.close()

                response = 'HTTP/1.1 200 OK \n\n' + outputdata
                self.connectionSocket.sendall(response.encode())

            except IOError:
                response = 'HTTP/1.1 404 Not Found\n\nFile Not Found'
                self.connectionSocket.sendall(response.encode())

        time.sleep(4)
        # self.connectionSocket.sendall(response.encode())
        # self.connectionSocket.close()

    def stop(self):
        self.running = False
        self.connectionSocket.close()