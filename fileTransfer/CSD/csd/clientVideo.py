'''import bluetooth,subprocess
import lightblue  
# we should know  
target_name = "DESKTOP-V0NC588"  
file_to_send = "file.txt"  
    
# we don't know yet  
obex_port = None                 
target_address = None  
    
print "searching for nearby devices..."  
nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True,
                                                      flush_cache=True, lookup_class=False)

name = "DESKTOP-V0NC588"      # Device name
addr = addr      # Device Address
port = 1         # RFCOMM port
passkey = "1111" # passkey of the device you want to connect

# kill any "bluetooth-agent" process that is already running
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr,port))
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass
s.recv(1024) # Buffer size
s.send("Hello World!")'''
import socket

HOST = '192.168.43.115'
PORT = 8002
ADDR = (HOST,PORT)
BUFSIZE = 4096
videofile = "/home/chadalavada/Desktop/test.mp4"

bytes = open(videofile,'rb').read()

print len(bytes)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(bytes)

client.close()