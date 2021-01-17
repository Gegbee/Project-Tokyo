// Finalized script for the Arduino car, combines the bluetooth module (HC-05), the motor controller (L298N), two DC motors, and an Arduino Uno.

#define enB 9
#define in4 5
#define in3 4

#define enA 8
#define in2 3
#define in1 2

void setup() {
  Serial.begin(38400);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  Serial.setTimeout(15);
}

void loop() {
 if (Serial.available() > 0) {
   String data = Serial.readString();
   String r = data.substring(0, data.indexOf("|"));
   String l = data.substring(data.indexOf("|") + 1);
   if ((l.toInt() + r.toInt()) > 0) {
     analogWrite(enA, l.toInt());
     analogWrite(enB, r.toInt());
   }
 }
}