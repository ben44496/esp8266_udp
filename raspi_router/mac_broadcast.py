import socket
import time
import os

print("Broadcast Raspi")

serverAddressPort = ("10.1.10.14", 4210)
bufferSize = 1024
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up new Socket
UDPServerSocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

gw = os.popen("ip -4 route").read().split() # Run cmd to find IP Addresses
#UDPServerSocket.connect(serverAddressPort)
myIP = socket.gethostbyname(socket.gethostname())#UDPServerSocket.getsockname()[0] # Get ip address of current device
myName = socket.gethostname() # Get hostname of device
#gateway = gw[2] # gateway ip address



#print("Host IP:",myIP," GW:",gateway," Host:", myName)
print("Server IP Socket: ", serverAddressPort[0])

def broadcast_Message(message):
    UDPServerSocket.sendto(message, serverAddressPort)




while(1):
    #UDPServerSocket.sendto(123, serverAddressPort)
    broadcast_Message(b"I love zero two")
    print("Ilovezerotwo")
    time.sleep(1)
    



