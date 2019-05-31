import socket
import bluetooth  
import lightblue

HOST = '192.168.43.114'
PORT = 8004
ADDR = (HOST,PORT)
BUFSIZE = 4096
file1 = '' 

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

while True:
        conn, addr = serv.accept()
        print 'client connected ... ', addr
        i=1
        while True:
                data = conn.recv(BUFSIZE)
                print data
                if i==1:
                        if data == '1':
                                myfile = open('testfile.txt', 'w')
                                file1 = 'testfile.txt'
                        elif data == '2':
                                myfile = open('testfile.jpeg', 'w')
                                file1 = 'testfile.jpeg'
                        elif data == '3':
                                myfile = open('testfile.MOV', 'w')
                                file1 = 'testfile.MOV'
                        i = 0
                else:
                        if not data: break
                        myfile.write(data)
                        print 'writing file ....'
        myfile.close()
        print 'finished writing file'
        conn.close()
        print 'client disconnected'