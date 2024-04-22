import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Function to encrypt data and send it to the server
def encrypt_and_send(conn, session_key, data):
    # Encrypt the data using the session key
    cipher = Cipher(algorithms.AES(session_key), modes.CFB(b'RandomInitVector'), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Send the encrypted data to the server
    conn.send(encrypted_data)

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

try:
    # Receive the session key from the server
    session_key = client_socket.recv(4096)

    # Encrypt and send data to the server
    with open("TestingServer.html", "rb") as f:
            data_to_send = f.read()
    #data_to_send = "Hello, Server! This is my encrypted message."
    encrypt_and_send(client_socket, session_key, data_to_send)

finally:
    # Close the connection
    client_socket.close()
