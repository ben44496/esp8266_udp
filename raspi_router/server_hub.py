import socket
import time


print('Hello World')

serverAddressPort =("10.1.10.255", 4210)
bufferSize = 1024
serverIP = '0.0.0.0'
serverSSID = "unknown"

# Get hostname ssid and ip address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        serverSSID = host_name
        print("Hostname : ",serverSSID)
        serverIP = host_ip
        print("IP : ",serverIP)
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




get_Host_name_IP() # Set ipaddress and ssid


# Create a UDP Socket
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.bind(serverAddressPort)


# Receive Message
while(1):
    receive_Message(UDPClientSocket)
    ##time.sleep(1)

