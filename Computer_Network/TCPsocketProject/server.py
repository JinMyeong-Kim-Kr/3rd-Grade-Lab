from socket import *
import time

HOST = "localhost"
PORT = 80
DAY_NAME = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ExceptFileNotFound sends an error message to the client when a FileNotFound error occurs.
def ExceptFileNotFound(client_socket):
    status = 'HTTP/1.1 400 Bad Request\r\n'
    message = '<html><title>Error: File Not Found</title></html>'
    content_length = str(len(message)) + '\r\n\r\n'
    if http_method == "HEAD":
        client_socket.send((status + host + date + content_type + content_length).encode('utf-8'))
    else:
        client_socket.send((status + host + date + content_type + content_length + message).encode('utf-8'))

# @server_socket is a tcp socket object that uses localhost and port number 80.
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(0)
                                                      
while True:
    try:
        print("Waiting for client request ... ")
        # @client_socket is a client socket object requested by @server_socket.
        client_socket, _ = server_socket.accept()
        client_socket.settimeout(10)
        # @now represents the time requested by the client.
        now = time
        # @chunk is data received from the @client_socket.
        chunk = client_socket.recv(1024)
        # If there is no response for 10 seconds, an exception is made.
    except Exception:
        print('HTTP/1.1 408 Request Timeout\r\n\r\n')
        status = 'HTTP/1.1 408 Request Timeout\r\n\r\n'
        message = '<html><title>Error: Request Timeout</title></html>'
        client_socket.send((status + message).encode('utf-8'))
        client_socket.close()   
        server_socket.close()
        exit()
    
    # List of HTTP header fields:
    # Status(@status)
    # Host(@host)
    # Date(@date)
    # Content-Type(@content_type)
    # Content-Length(@content_length)
    # <empty line>
    # body

    data = chunk.decode("utf-8")
    # client exit
    if data == "":
        print("Close the server.")
        client_socket.close()
        server_socket.close()
        exit()
    request_message = data.split("\r\n")
    request_line = request_message[0].split(" ")

    host = request_message[1] +'\r\n'
    date = f'Date: {DAY_NAME[now.gmtime().tm_wday]}, {now.gmtime().tm_mday} {MONTH[now.gmtime().tm_mon - 1]} {now.gmtime().tm_year} {now.gmtime().tm_hour}:{now.gmtime().tm_min}:{now.gmtime().tm_sec} GMT \r\n'
    content_type = 'Content-Type: text/html\r\n'

    # @http_method is a variable that stores the HTTP request method requested by the client.
    http_method = request_line[0]

    # GET method responds to the client with data from @file and HTTP header fields.
    if http_method == "GET":
        try:
            filename = request_line[1]
            file = open('.'+filename, encoding='utf-8')
        except FileNotFoundError:
            ExceptFileNotFound(client_socket)
            client_socket.close()
            server_socket.close()
            exit()
        else:
            print("received a GET request from the client.")
            status = 'HTTP/1.1 200 OK\r\n'
            content = file.read()
            file.close()
            content_length = f'Content-Length: {str(len(content))}\r\n\r\n'
            client_socket.send((status + host + date + content_type + content_length + content).encode('utf-8'))

    # PUT method adds the requested content from the client to @file and responds HTTP header fields.
    elif http_method == "PUT":
        try:
            filename = request_line[1]
            file = open('.' + filename, encoding = 'utf-8')
        except FileNotFoundError:
            ExceptFileNotFound(client_socket)
            client_socket.close()
            server_socket.close()
            exit()
        else:
            file.close()

            print("received a PUT request from the client.")
            status = 'HTTP/1.1 200 OK\r\n'
            content = request_message[-1]
            file = open('.' + filename, 'a', encoding = 'utf-8')
            file.write('<h1> '+ content + ' </h1>\n')
            file.close()

            file = open('.'+ filename, 'r', encoding = 'utf-8')
            content = file.read()
            content_length = f'Content-Length: {str(len(content))}\r\n\r\n'
            file.close()
            client_socket.send((status + host + date + content_type + content_length + content).encode('utf-8'))

    # HEAD method responds to the client with HTTP header fields.
    elif http_method == "HEAD":
        try:
            filename = request_line[1]
            file = open('.'+ filename, encoding = 'utf-8')

        except FileNotFoundError:
            ExceptFileNotFound(client_socket)
            client_socket.close()
            server_socket.close()
            exit()

        else:
            print("received a HEAD request from the client.")
            status = 'HTTP/1.1 200 OK\r\n'
            content = file.read()
            file.close()
            content_length = f'Content-Length: {str(len(content))}\r\n\r\n'
            client_socket.send((status + host + date + content_type + content_length).encode('utf-8'))

    # POST method initializes @file and add @content.
    elif http_method == "POST":
        try:
            filename = request_message[-1].split('&')[0].split('=')[-1]
            file = open('.'+ filename, encoding = 'utf-8')
        except FileNotFoundError:
            ExceptFileNotFound(client_socket)
            client_socket.close()
            server_socket.close()
            exit()
        else:
            file.close()

            print("received a POST request from the client.")
            status = 'HTTP/1.1 201 Created\r\n'
            content = request_message[-1].split('&')[1].split('=')[-1]
            file = open('.'+ filename, 'w', encoding = 'utf-8')
            file.write('<h1> '+ content + ' </h1>\n')
            file.close()

            file = open('.'+ filename, 'r', encoding = 'utf-8')
            content = file.read()
            content_length = f'Content-Length: {str(len(content))}\r\n\r\n'
            file.close()
            client_socket.send((status + host + date + content_type + content_length + content).encode('utf-8'))

    else:
        status = 'HTTP/1.1 400 Bad Request\r\n'
        message = '<html><title>Error: Invalid HTTP request</title></html>'
        content_length = str(len(message)) + '\r\n\r\n'
        client_socket.send((status + host + date + content_type + content_length + message).encode('utf-8'))
        print('HTTP/1.1 400 Bad Request\r\n\r\n')       
        client_socket.close()
        server_socket.close()
        exit()
