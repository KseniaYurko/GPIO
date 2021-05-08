#include <Arduino.h>
  
  int LED[8] = {9, 8, 7, 6, 5, 4, 3, 2};
  int LedNumber = 2;
  float period = 0.5;

int LightUp(int LedNumber, float period)
{
  digitalWrite(LED[Lednumber-1], HIGH);
  delay(period*1000);
  digitalWrite(LED[Lednumber-1], LOW);
}

void setup()
{  
  for (int i; i<9; i++)
  {
    pinMode(i, OUTPUT);
  }
  LightUp(LedNumber, period)
}