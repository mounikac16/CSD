import socket

HOST = '192.168.43.122'
PORT = 8003
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

while True:
  conn, addr = serv.accept()
  print 'client connected ... ', addr
  myfile = open('testfile.txt', 'wb')

  while True:
    data = conn.recv(BUFSIZE)
    if not data: break
    myfile.write(data)
    print 'writing file ....'

  myfile.close()
  print 'finished writing file'
  conn.close()
print 'client disconnected'
