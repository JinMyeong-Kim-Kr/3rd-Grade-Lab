from socket import *

IP = "localhost"
PORT = 80
FILE_NAME = "todo.html"

# Check_4xx prints an error message and exits program if the response code received from the server is 4xx.
def Check_4xx(data):
    data = data.decode('utf-8')
    if data == "b''" or data == '' or int(int(data.split(" ")[1]) / 100) != 2:
        print(data)
        client_socket.close()
        exit()
    else:
        print(data)

while True:
    try:
        # @client_socket is a tcp socket object that uses localhost and port number 80.
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((IP, PORT))
    except:
        client_socket.close()
        print('HTTP/1.1 500 Internal Server Error\r\n\r\n')
        exit()

    print("1. See to-do list(GET) \n2. Add to-do item(PUT) \n3. Request HTTP header data(HEAD) \n4. Initialize to-do list(POST) \n5. Exit")
    request_method = int(input("Enter http request method > "))

        # GET request requests data for @FILE_NAME as an HTTP protocol GET request from the server.
    if request_method == 1:
        header = f'GET /{FILE_NAME} HTTP/1.1\r\nHost:"{IP}"\r\n\r\n'
        client_socket.send(bytes(header, encoding = 'utf-8'))
        data = client_socket.recv(1024)
        Check_4xx(data)

        client_socket.close()
    # PUT request create a new file on the server with the file name @FILE_NAME, and add @content.
    elif request_method == 2:
        content = str(input("Enter add list >"))
        header = f'PUT /{FILE_NAME} HTTP/1.1\r\nHost:"{IP}"\r\nContent-Type: text/html\r\nContent-Length: {len(content)}\r\n\r\n'
        body = bytes(content, encoding = 'utf-8')
        client_socket.send(bytes(header, encoding = 'utf-8') + body)
        
        data = client_socket.recv(1024)
        Check_4xx(data)
        client_socket.close()

    # HEAD request requests response header data but does not include the body of the response.
    elif request_method == 3:
        header = f'HEAD /{FILE_NAME} HTTP/1.1\r\nHost:"{IP}"\r\n\r\n'
        client_socket.send(bytes(header, encoding = 'utf-8'))
        data = client_socket.recv(1024)

        Check_4xx(data)
        client_socket.close()
    
    # POST request requests to add @content to @FILE_NAME.
    elif request_method == 4:
        content = str(input("Enter add list >"))
        header = f'POST / HTTP/1.1\r\nHost:"{IP}"\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(content)}\r\n\r\n'
        body = f'filename=/{FILE_NAME}&content={content}'
        client_socket.send(bytes(header, encoding = 'utf-8') + bytes(body, encoding = 'utf-8'))

        data = client_socket.recv(1024)
        Check_4xx(data)
        client_socket.close()

    elif request_method == 5:
        client_socket.close()
        exit()

    else:
        print("Wrong number")
        client_socket.close()
        exit()




