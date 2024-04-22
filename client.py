# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:55:27 2024

@author: johnm
"""

import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send data to the server
message = "Hello, server!"
client_socket.sendall(message.encode('utf-8'))

# Receive a response from the server
data = client_socket.recv(1024)
print("Received from server:", data.decode('utf-8'))

# Close the connection
client_socket.close()
