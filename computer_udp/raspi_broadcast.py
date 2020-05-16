import socket
import time
import os

print("Broadcast Raspi")

MESSAGE = b"I love zero two"
serverAddressPort = ("10.1.10.255", 4210) # Send to broadcast IP at port Port
bufferSize = 1024
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up new Socket
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1) # Set setting for permissions to broadcast to broadcast IP


myIP = socket.gethostbyname(socket.gethostname()) 
# Get ip address of current device
myName = socket.gethostname() # Get hostname of device




print("My IP:",myIP," My SSID:", myName)
print("Broadcast at: ", serverAddressPort[0]," Port: ",serverAddressPort[1])

print("Make sure you have correctly copied the Broadcast IP")
def broadcast_Message(message):
    UDPServerSocket.sendto(message, serverAddressPort)



while(1):
    #UDPServerSocket.sendto(123, serverAddressPort)
    broadcast_Message(MESSAGE)
    print("Ilovezerotwo")
    time.sleep(1)
    



