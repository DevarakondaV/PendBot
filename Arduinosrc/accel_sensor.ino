/*
This file is arduino implementation that uses an led and photoresistor to
determine the rpm of a wheel
*/


//Dependencies
#include <Time.h>


//Some Globals
const int ledPin = 8;
const int photoPin = 0;
String valStr;
time_t t;

void setup() {
  //Defining pin modes
  pinMode(ledPin,OUTPUT);
  pinMode(photoPin,INPUT);
  
  //Setting LED high
  digitalWrite(ledPin,HIGH);
  
  //Begin Serial Monitor
  Serial.begin(9600);
}

void loop() {
  //val = analogRead(photoPin);
  //valStr = String(val,DEC);
  Serial.println("Seconds: "+String(second(),DEC)+"\t PhotoResistor Voltage: "+String(analogRead(photoPin),DEC));
}
