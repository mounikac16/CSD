import socket

s=socket.socket()
host = '192.168.43.115'
print(host)
port = 8002
s.bind((host,port))

s.listen(5)
while True:
        c,addr = s.accept()
        print("got connection from",addr)
        c.send(b'file transferred') 
        c.close()       
