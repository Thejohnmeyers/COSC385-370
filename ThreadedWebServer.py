import socket
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]

        with open(filename[1:], 'r') as f:
            outputdata = f.read()

        connectionSocket.send('\nHTTP/1.1 200 OK\r\n\r\n'.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        file2 = open("404ErrorPage.html")
        outp = file2.read()

        connectionSocket.send("\nHTTP/1.1 404 Not Found\r\n\r\n".encode())
        for i in range(0, len(outp)):
            connectionSocket.send(outp[i].encode())
        connectionSocket.send("\r\n".encode())
    finally:
        connectionSocket.close()

# Create a TCP server socket
serverPort = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Prepare a server socket
public_ip = socket.gethostbyname(socket.gethostname())
print(public_ip)
serverSocket.bind((public_ip, serverPort))
serverSocket.listen(5)
print('The web server is up on port:', serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    # Create a new thread for each client request
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()
