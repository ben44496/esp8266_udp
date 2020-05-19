import socket
import time
import os



print('Router Collection Bin')

myAddressPort = ("",0)
bufferSize = 1024
myIP = '0.0.0.0'
mySSID = "unknown"
numDrones = 4
startPort = 4210
queueSize = 1000
drone = {}



#################################Define Function###############################

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


#def threading():
    

# Receive Messages from Server
def receive_Message(UDPSocket):
    """UDPSocket.bind(set_myAddress(port))"""
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    s = bytesAddressPair[0]
    ip = bytesAddressPair[1]
    pmsg = "Message from Server:{}".format(s)
    pip = "ServerIP Address:{}".format(ip)
    print(pmsg)
    #print(pip)
    return bytesAddressPair

def update(pair):
    ip = pair[1][0]
    port = pair[1][1]
    drone.update({ip:pair})
    print(drone.items())

################################# START SCRIPT #################################

# Setup
get_Host_Name_IP() # Print this computer's information
set_myAddress_Default(4210) # Listen on port 4210 at every IP (for broadcast)


# Create a UDP Socket
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.bind(myAddressPort) # Binds your IP to listen in on a current port.


#print(UDPClientSocket.getsockname()) # Prints IP Address and port


# Receive Message
while(1):
    update(receive_Message(UDPClientSocket))
    ##time.sleep(1)

