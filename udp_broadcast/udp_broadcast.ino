#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

//const char* ssid = "NETGEAR_11N";
//const char* password = "sharedsecret";
const char* ssid = "DronePi";
const char* password = "dronegod";

WiFiUDP udp;
unsigned int listenPort = 4210;  // local port to listen on
unsigned int broadcastPort = 4210;
char incomingPacket[255];  // buffer for incoming packets
char  sendPacket[] = "zerotwo is my darling.";  // a reply string to send back


void setup()
{
  Serial.begin(115200);
  Serial.println("Code Start.");

  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");
  
  udp.begin(broadcastPort);
  Serial.printf("Now boradcasting at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), broadcastPort);
}


void loop()
{
  //broadcast char array
  IPAddress myIP = WiFi.localIP();
  myIP[3] = 255;
  //Serial.println(myIP);
  
  sendMessage("zerotwoismydarling", myIP, broadcastPort);
  




  /* //Debug Code
    Serial.print("Sending packet: ");
    boolean check = Udp.beginPacket("10.1.10.250", 4210);
    if(check){
    Udp.write(sendPacket);
    Serial.println(sendPacket);
    }
    Udp.endPacket();
    yield();
    */
}

void sendMessage(char* message, IPAddress ip, int port){
  udp.beginPacket(ip, port);
  udp.write(message);
  Serial.println(message);
  udp.endPacket();
  yield();
}
