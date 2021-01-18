#include <LiquidCrystal.h>
#include <SoftwareSerial.h>
SoftwareSerial SUART(6, 7);//SRX-pin/STX-pin of UNO

LiquidCrystal lcd(11, 12, 2, 3, 4, 5);

void setup() {
  Serial.begin(9600);
  SUART.begin(9600);
  lcd.begin(16, 2);
  analogWrite(10, 8);
  lcd.print("started!");
  SUART.println("Hello from bluetooth!");
}

void loop() {
  if (SUART.available() > 0) {
    String data = SUART.readString();
    lcd.clear();
    delay(20);
    lcd.print(data);
    delay(20);
  }
}
