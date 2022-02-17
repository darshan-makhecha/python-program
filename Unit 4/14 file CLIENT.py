import socket                   		# Import socket module

s = socket.socket()             		# Create a socket object
host = socket.gethostname()     	# Get local machine name
IP = socket.gethostbyname(host) 
port = 60000                    		# Reserve a port for your service.
print(IP)
s.connect((IP, port))
s.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print(b'Successfully get the file')
s.close()
print(b'connection closed')
