'''
import socket

HOST = '172.20.10.3'         # server ip
PORT = 42050              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print "Server running", HOST, PORT
s.listen(5)
conn, addr = s.accept()
print'Connected by', addr

while True:
    data = "".join(iter(lambda:conn.recv(1)))       
    print data   
    if not data: break                
      
print "Done Receiving"
conn.close()
'''
'''
# server.py

import socket                   # Import socket module

port = 8002                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('192.168.225.30', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='Face_Recognition.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()'''

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()