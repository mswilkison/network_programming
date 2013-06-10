import socket
hostname = 'maps.googleapis.com'
addr = socket.gethostbyname(hostname)
print 'The address of', hostname, 'is', addr
