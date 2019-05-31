import socket
from time import sleep
HOST = '192.168.43.115'
PORT = 8002
ADDR = (HOST,PORT)
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting..."
client.connect(ADDR)

opp=raw_input("Enter code : ")
if opp == 1 :
	file = "/home/chadalavada/Desktop/csd/test.txt"
elif opp == 2:
	file = "/home/chadalavada/Desktop/csd/test.jpeg"
elif opp == 3:
	file = "/home/chadalavada/Desktop/csd/test1.MOV"

bytes = open(file,'r').read()
#print "File size in bytes : ",len(bytes)

print "sending..."
client.send(str(opp))
sleep(2)
print "file sending..."
client.send(bytes)

print "file sent"
client.close()