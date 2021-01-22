// Script for the Arduino car, combines the bluetooth module (HC-05), the motor controller (L298N), two DC motors, and an Arduino Uno.
#include <SoftwareSerial.h>

#define enB 10
#define in4 2
#define in3 3

#define enA 11
#define in2 4
#define in1 5

int amt = 0;

int r = 0;
int l = 0;
int t = 0;
void setup() {
  Serial.begin(9600); //COM3
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  Serial.setTimeout(15);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    r = data.substring(0, data.indexOf("|")).toInt();
    l = data.substring(data.indexOf("|") + 1, data.indexOf("/")).toInt();
    t = data.substring(data.indexOf("/") + 1).toInt();
    if (t == 0) {
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
    } else {
      digitalWrite(in2, HIGH);
      digitalWrite(in1, LOW);
      digitalWrite(in4, HIGH);
      digitalWrite(in3, LOW);
    }
    analogWrite(enB, l);
    analogWrite(enA, r);
  } 
}
