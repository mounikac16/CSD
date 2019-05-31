import socket
from time import sleep
HOST = '192.168.43.65'
PORT = 8003
ADDR = (HOST,PORT)
BUFSIZE = 4096

#print len(bytes)
opp=raw_input("Enter code : ")

if opp == '1' :
	file = "testfile.txt"
elif opp == '2':
	file = "testfile.jpeg"
elif opp == '3':
	file = "testfile.MOV"


bytes = open(file,'rb').read()

print bytes

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting..."
client.connect(ADDR)

print "sending..."
client.send(str(opp))
sleep(2)
print "file sending..."
client.send(bytes)

print "file sent"
client.close()

bytes=""
