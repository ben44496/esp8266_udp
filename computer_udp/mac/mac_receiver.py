import socket
import time
import os


print('Mac UDP Receiver')

serverAddressPort = ("0.0.0.0",0)
bufferSize = 1024
clientIP = '0.0.0.0'
clientSSID = "unknown"


# Get hostname ssid and ip address
def get_Host_name_IP(socketNumber):
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        clientSSID = host_name
        print("Hostname : ",clientSSID)
        clientIP = host_ip
        print("Host IP : ",clientIP)
        serverAddressPort = (clientIP, socketNumber)
    except:
        print("Unable to get Hostname and IP")
    


# Receive Messages from Server
def receive_Message(UDPSocket):
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    s = bytesAddressPair[0]
    ip = bytesAddressPair[1]
    pmsg = "Message from Server:{}".format(s)
    pip = "ServerIP Address:{}".format(ip)
    print(pmsg)
    print(pip)

######## START SCRIPT ########


#get_Host_name_IP(4210) # Set ipaddress and ssid; attach to port 4210


# Create a UDP Socket
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.bind(("",4210))
########UDPClientSocket.connect(("10.1.10.41",4210))
##UDPClientSocket.connect(("10.1.10.255",4210))
#UDPClientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

#UDPClientSocket.bind(("192.168.86.24",4210))
#UDPClientSocket.connect(("192.168.86.254",4210))
#serverip = UDPClientSocket.getsockname()[0]
#serverport = UDPClientSocket.getsockname()[1]
#gateway = gw[2]
#host = socket.gethostname()
#print ("Server IP:",serverip," GW:",gateway," Port:",serverport, " Host:",hosto)
print(UDPClientSocket.getsockname())


# Receive Message
while(1):
	receive_Message(UDPClientSocket)
	#print(UDPClientSocket.recvfrom(1024)[0])   
##time.sleep(1)
