#include <LiquidCrystal.h>

LiquidCrystal lcd(11, 12, 2, 3, 4, 5);

void setup() {
  Serial.begin(38400);
  lcd.begin(16, 2);
  analogWrite(10, 8);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    lcd.clear();
    delay(20);
    lcd.print("HI!!");
    delay(20);
  }
}
