import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Function to receive data from the client and decrypt it
def receive_and_decrypt(conn, session_key):
    # Receive the encrypted data from the client
    encrypted_data = conn.recv(4096)

    # Decrypt the data using the session key
    cipher = Cipher(algorithms.AES(session_key), modes.CFB(b'RandomInitVector'), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    return decrypted_data

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('', 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

# Accept incoming connection
print("Waiting for a connection...")
connection, client_address = server_socket.accept()
print("Connection established with", client_address)

try:
    # Generate a session key for encryption
    session_key = b'ThisIsASecretKey'

    # Send the session key to the client
    connection.send(session_key)

    # Receive and decrypt data from the client
    decrypted_data = receive_and_decrypt(connection, session_key)
    with open("decrypted_example.html", "wb") as f:
        f.write(decrypted_data)
    #print("Received decrypted data from client:", decrypted_data.decode())

finally:
    # Close the connection
    connection.close()
