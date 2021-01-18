// Script for the Arduino car, combines the bluetooth module (HC-05), the motor controller (L298N), two DC motors, and an Arduino Uno.
#include <SoftwareSerial.h>
SoftwareSerial Commune(6, 7);

#define enB 9
#define in4 5
#define in3 4

#define enA 8
#define in2 3
#define in1 2

void setup() {
  Commune.begin(9600); //COM4
  Serial.begin(9600); //COM3
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  Commune.setTimeout(15);
}

void loop() {
  if (Commune.available() > 0) {
    String data = Commune.readString();
    String r = data.substring(0, data.indexOf("|"));
    String l = data.substring(data.indexOf("|") + 1);
    Serial.print(r);
    Serial.println(l);
    analogWrite(enA, l.toInt());
    analogWrite(enB, r.toInt());
  }
}