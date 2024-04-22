# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:55:23 2024

@author: johnm
"""

import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on {}:{}".format(*server_address))

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print("Connection from", client_address)

    # Receive data from the client
    data = client_socket.recv(1024)
    print("Received:", data.decode('utf-8'))

    # Send a response back to the client
    message = "Hello, client!"
    client_socket.sendall(message.encode('utf-8'))

    # Close the connection
    client_socket.close()
    