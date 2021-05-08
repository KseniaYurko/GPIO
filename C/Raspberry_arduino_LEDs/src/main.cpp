#include <Arduino.h>

void setup()
{
  pinMode(4, OUTPUT);
}

void loop()
{
  digitalWrite(4, LOW);
  delay(period*1000)
  digitalWrite(4, LOW);
}