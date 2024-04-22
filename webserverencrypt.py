import http.server
import socketserver
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Define the port you want to run the server on
PORT = 8000

# Define the key and initialization vector for encryption
KEY = b'thisIsASecretKey'
IV = b'RandomInitVector'

# Define the handler to handle incoming requests
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        # Set the response status code
        self.send_response(200)
        
        # Set the content type of the response
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Read the file content
        with open("TestingServer.html", "rb") as f:
            file_content = f.read()
        
        # Encrypt the file content using AES encryption
        cipher = Cipher(algorithms.AES(KEY), modes.CFB(IV), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_content = encryptor.update(file_content) + encryptor.finalize()
        
        # Encode the encrypted content in base64 for transmission
        encoded_content = base64.b64encode(encrypted_content)
        print(encoded_content)
        # Send the encrypted content as the response
        self.wfile.write(encoded_content)

# Create a TCP server
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Server running on port", PORT)
    
    # Start the server
    httpd.serve_forever()