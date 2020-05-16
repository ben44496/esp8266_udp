import socket
import time
import os


print('Hello World')

myAddressPort = ("",0)
bufferSize = 1024
myIP = '0.0.0.0'
mySSID = "unknown"
gw = os.popen("ip -4 route show default").read().split()


# Get hostname ssid and ip address
def get_Host_Name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        mySSID = host_name
        print("Hostname : ",mySSID)
        myIP = host_ip
        print("Host IP : ",myIP)
    except:
        print("Unable to get Hostname and IP")


# Use this function to set up who you are and which port you are going to receive on.
def set_myAddress(port):
    global myAddressPort
    global myIP
    myAddressPort = (myIP,port)

def set_myAddress_Default(port):
    global myAddressPort
    myAddressPort = ("",port)


# Receive Messages from Server
def receive_Message(UDPSocket):
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    s = bytesAddressPair[0]
    ip = bytesAddressPair[1]
    pmsg = "Message from Server:{}".format(s)
    pip = "ServerIP Address:{}".format(ip)
    print(pmsg)
    print(pip)

############################## START SCRIPT ##########################

# Setup
get_Host_Name_IP() # Print this computer's information
set_myAddress_Default(4210) # Listen on port 4210 at every IP (for broadcast)


# Create a UDP Socket
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.bind(myAddressPort) # Binds your IP to listen in on a current port.


serverIP = UDPClientSocket.getsockname()[0]
serverPort = UDPClientSocket.getsockname()[1]
print(UDPClientSocket.getsockname())


# Receive Message
while(1):
    receive_Message(UDPClientSocket)
    ##time.sleep(1)

