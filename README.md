# Web Server and Client on Python
Multithreaded Web Server and Single-threaded Client implementation on Python

## Description

This enables the user to run a multithreaded web server that would be able to handle multiple requests concurrently. The client initiates a connection to the server and would display then message status and page content of the requested file. 

## Getting Started
The server and client should work on Python 3.x. The web server can be tested on any browser (*Chrome recommended*).

### Running the Server

The server can be initialized on the command line using the following syntax

```
python -m server.py
```

This can be tested in a Web browser to get a page from the server. For example:

```
http://localhost:8000/index.html
```

If the file requested is not on the server, it will show a 404 File Not Found Error.

### Using the client

As the server is running, the client can be used instead of the browser to get files using the following syntax,

```
client.py <server_IPaddress> <port_no> <filename>
```

For example,

```
client.py localhost 8000 index.html
```

Similar to using the browser, it will show a 404 File Not Found error if requested file is not on the server.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/download/) - IDE used

### Packages, Modules, Etc.
* [socket](https://docs.python.org/3/library/socket.html) - Python's socket module
* SocketThread - Socket thread class I created for multithreading (*see SocketThread.py*)

#### Sources:
* Kurose, J. F., & Ross, K. W. (2012). Computer networking: A top-down approach.
* [RTT time](https://www.geeksforgeeks.org/program-calculate-round-trip-time-rtt/)
* [Web Server](http://joaoventura.net/blog/2017/python-webserver/)
* [Getting socket information](https://pymotw.com/2/socket/addressing.html)
* Socket Multithreading - [Link 1
](https://www.geeksforgeeks.org/socket-programming-multi-threading-python/) | [Link 2](https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/)

## Authors
* **Chezka Sino** - [Github](https://github.com/chezka-sino) | [LinkedIn](https://www.linkedin.com/in/chezka-sino/)