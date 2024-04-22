import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Define the URL of the server
URL = "http://localhost:8000"

# Define the key and initialization vector (IV) for decryption (should match the ones used for encryption)
KEY = b'thisIsASecretKey'
IV = b'RandomInitVector'

# Send a GET request to the server
response = requests.get(URL)

# Decode the response content from base64
encoded_content = response.content
print(encoded_content)
encrypted_content = base64.b64decode(encoded_content)

# Decrypt the content using AES decryption
cipher = Cipher(algorithms.AES(KEY), modes.CFB(IV), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_content = decryptor.update(encrypted_content) + decryptor.finalize()

# Write the decrypted content to a file
with open("decrypted_example.html", "wb") as f:
    f.write(decrypted_content)
