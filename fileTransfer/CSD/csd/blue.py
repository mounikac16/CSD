import bluetooth  
import lightblue  
# we should know  
target_name = "Galaxy Note8"  
file_to_send = "/home/chadalavada/Desktop/test.mp4"  
    
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
lightblue.obex.sendfile( target_address, service[1], file_to_send )  
'''try:  
    lightblue.obex.sendfile( target_address, service[1], file_to_send )  
    print "completed!\n"  
except:  
    print "an error occurred while sending file\n"'''
'''
import subprocess
import os
import re
from time import sleep
import sys
from Bluetoothctl import Bluetoothctl
 
DEVICE_MAC = '94:e9:79:c0:40:6b'
 
 
def getDeviceConnectionStatus():
    output = os.popen('pacmd list-cards').read()
    indexRegex = 'index\:\s(.*)\s+name\:\s<bluez_card.' + DEVICE_MAC.replace(':', '_')
    index = re.search(indexRegex, output).group(1)
 
    useless,main = output.split('device.string = "' + DEVICE_MAC + '"')
    profileRegex = 'active\sprofile:\s\<(.*)\>\s+'
    profile = re.search(profileRegex, main).group(1)
    return [index, profile]
 
data = [8, 'off']
while(data[1] == 'off'):
    # print os.system('sudo systemctl restart bluetooth')
    print('Restarting bluetooth...')
    subprocess.call(['sudo', 'systemctl', 'restart', 'bluetooth'])
    sleep(5)
    try:
        print('Connecting to device...')
        bl = Bluetoothctl()
        bl.connect(DEVICE_MAC)
    except:
        print('Error connecting to device...Retrying')
        continue
    sleep(7)
    try:
        print('Parsing status...')
        data = getDeviceConnectionStatus()
    except:
        print('Error parsing status...Retrying')
        continue
    print('Offline mode..Retrying' if data[1] == 'off' else 'A2DP Mode!! Finished!')
'''

'''
import sys
from bluetooth import *

HOST = '94:e9:79:c0:40:6b'       # The remote host
PORT = 5                 # Server port

s=BluetoothSocket( RFCOMM )

s.connect((HOST, PORT))

while True :
   message = raw_input('Send:')
   if not message : break
   s.send(message)
   data = s.recv(1024)
   print 'Received', `data`
s.close()'''