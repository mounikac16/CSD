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
'''
        # we should know  
        target_name = "Galaxy Note8"  
        file_to_send = "/home/chadalavada/Desktop/" + file1  
        # we don't know yet  
        obex_port = None                 
        target_address = None      
        print "searching for nearby devices..."  
        nearby_devices = bluetooth.discover_devices()  
        for bdaddr in nearby_devices:
                print bluetooth.lookup_name( bdaddr )
                if target_name == bluetooth.lookup_name( bdaddr ):
                        print "found the target device!"
                        target_address = bdaddr
                        break  
        #target_address = '94:e9:79:c0:40:6c'
        print target_address
        print "searching for the object push service..."  
        services = lightblue.findservices(target_address)  
        print services
        for service in services:  
            if service[2] == "OBEX Object Push":  
                obex_port = service[1]       
                print "OK, service '", service[2], "' is in port", service[1], "!"  
                break     
        print "sending a file..."  
        lightblue.obex.sendfile( target_address, service[1], file_to_send )  '''