import socket
sock = socket.socket()
sock.connect(('maps.googleapis.com', 80))
sock.sendall(
    'GET /maps/api/geocode/json?address=5903+Laurium+Rd%2C+Charlotte%2C+NC'
    '&sensor=false'
    'Host: maps.googleapis.com:80\r\n'
    'User-Agent: search2.py\r\n'
    'Connection: close\r\n'
    '\r\n')
rawreply = sock.recv(4096)
print rawreply
