import socket

HOST = '172.20.10.3'        # The remote host
PORT = 42050              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)2q
s.connect((HOST, PORT))
f = open('reservation.txt', 'rb')
print "Sending Data ...."  
l = f.read()
while True:      
    for line in l:
        s.send(line)    
    break
f.close()
print "Sending Complete"
s.close()
