#include "ESP8266WiFi.h"


const char* espSSID = "Drone0";
const char* espPASS = "";

void setup() {
  Serial.begin(115200);
  // Set WiFi to station mode and disconnect from an AP if it was previously connected
  //WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(2000);
  Serial.println("Setup done");
  establishWiFi();
}

void loop() {
  scanNearbyDrones();
}




void establishWiFi(){
  WiFi.softAP(espSSID, espPASS);
  Serial.print("Access Point \"");
  Serial.print(espSSID);
  Serial.println("\" started");

  Serial.print("IP address:\t");
  Serial.println(WiFi.softAPIP());
}

void scanNearbyDrones(){
//Serial.println("scan start");

  
  int n = WiFi.scanNetworks();// WiFi.scanNetworks will return the number of networks found
  //Serial.println("scan done");
  if (n == 0)
    Serial.println("no networks found");
  else
  {
//    Serial.print(n);
//    Serial.println(" networks found");
    
    for (int i = 0; i < n; ++i)
    {
      // Print SSID and RSSI for each network found
      if(WiFi.SSID(i).indexOf("Drone")>=0){
        Serial.print(i + 1);
        Serial.print(": ");
        Serial.print(WiFi.SSID(i));
        Serial.print(" (");
        Serial.print(WiFi.RSSI(i));
        Serial.print(")");
        Serial.println((WiFi.encryptionType(i) == ENC_TYPE_NONE)?" ":"*");
        delay(10);
      }
    }
  }
  Serial.println("");

  // Wait a bit before scanning again
  delay(1000);
}
