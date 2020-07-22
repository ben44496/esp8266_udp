# esp8266_udp
###### **This is a library intended for UDP communication between ESP8266, RasPi, and Linux/Mac**

This library holds code for communication between different nodes on a UDP network. Please see wikipedia and youtube for information on UDP packets if you are new. 

## UDP Packets
The User Datagram Protocol (UDP) is a structure developed in the early day of the internet to facilitate packet transfer for files that did not require an acknowledge statement 
after receiving (as opposed to TCP). During development of a wireless mesh network and research into such a structure for a decentralized drone network, I found UDP to be 
the perfect tool for relaying time-dependent state information. Most of the time, the drones would only need to relay either their position and state information to local
neighbors to prevent any crashes. UDP works best here because neighboring drones only care about the most up-to-date information, and if a packet is lost (bad or weak signal) and 
a new packet is sent, this new packet should replace the lost packet anyways. Furthermore, this assumes that we do not really care about signal loss, as weak signals usually indicate
that the drones are not close to each other anyways.

This ReadMe is not intended to familiarize the reader with UDP, but rather to offer insight into the library and reasons for UDP. To learn more about UDP, please refer to the
following sources below.
- [TCP vs. UDP](https://www.youtube.com/watch?v=uwoD5YsGACg)
- [Wikipedia](https://en.wikipedia.org/wiki/User_Datagram_Protocol)

## ESP 8266
The ESP 8266 is an open-sourced arduino compatible board that has the additional benefit of support WiFi. With this capability and the lack of any inherent security on 
WiFi networks other than basic password (as opposed to Bluetooth authentication), I choose WiFi to perform a test of the functionality of a wireless mesh network on a 
drone swarm. 

## Using the library
For computer related code (RasPi, Linux/Mac), please refer to the *computer_udp* folder. 
To run files, open up terminal on your OS and type
```
python3 [file_name].py
```
where file_name is the name of the file you want to run. For example, you would change ***file_name*** to ***raspi_broadcast*** if you wanted to run it.
This will begin to run the code. **Please make sure that it is listening on the correct port and network (SSID/Password), changing it in the code at the variable declarations.**

For ESP8266 cpp Arduino code, please refer to the *esp8266_udp* folder
Connect your ESP8266, open up the file in Arduino IDE, and flash the program. If you are connected to computer, you can also open up Serial Monitor to see the print statements. 
Once you have flashed the ESP8266, the next time you connect to a power supply it will automatically run the program. **Please make sure that it is listening on the correct port and network (SSID/Password), changing it in the code at the variable declarations.**
## Dependencies
Please refer to this website or your specific board website for ESP8266 library dependencies.
- [ESP8266](https://dzone.com/articles/programming-the-esp8266-with-the-arduino-ide-in-3)

