
"""
Created on Mon Feb 19 15:33:41 2024

@author: johnm
"""


import socket

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverPort=12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print ('the web server is up on port:', serverPort)


while True:
	#Establish the connection

	print ('Ready to serve...')

	# Set up a new connection from the client
	connectionSocket, addr =serverSocket.accept() 

	try:

		message =connectionSocket.recv(1024)  

		filename = message.split()[1]
		
		f = open(filename[1:])

		outputdata =f.read() 
		#print (outputdata)
		
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		
		
		file2 = open("404ErrorPage.html")
		outp = file2.read()

		connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
		# Send the content of the 404 placeholder file to the connection socket
		for i in range(0, len(outp)):
			connectionSocket.send(outp[i].encode())
		connectionSocket.send("\r\n".encode())
		
		connectionSocket.close()
		
serverSocket.close()