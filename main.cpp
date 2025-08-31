#include "WiFi.h"  // Library - pre-written code for WiFi functions

int scan_count = 0;      // Which measurement cycle we're on
String name = "joris";

void setup() {
  Serial.begin(115200);        // Start communication at 115200 bits/second
  pinMode(5, OUTPUT);          // Set pin 5 as output so we can control LED
  WiFi.mode(WIFI_STA);         // Set WiFi to "station" mode (scan only, don't broadcast)
}

void loop() {
  digitalWrite(5, HIGH);       // Turn LED on (HIGH = 3.3V on ESP32)
  delay(100);                  // Wait 100 milliseconds
  digitalWrite(5, LOW);        // Turn LED off (LOW = 0V)
  
  int networks = WiFi.scanNetworks();  // Returns number (count) of WiFi networks found
  
  int detection_id = 0;
  for (int i = 0; i < networks; i++) {
    Serial.println(WiFi.SSID(i) + "," + WiFi.RSSI(i) + "," + detection_id + "," + scan_count + "," + name);     // SSID = network name, RSSI = signal strength (negative number, closer to 0 = stronger)  
    detection_id++;
  }
  scan_count++;
  delay(5000);  // Wait 5000 milliseconds (5 seconds)
}
