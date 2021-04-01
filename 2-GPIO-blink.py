import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (blinkCount):
        GPIO.output(N[ledNumber],1)
        time.sleep(blinkPeriod)
        GPIO.output(N[ledNumber],0)
        time.sleep(blinkPeriod)
ledNumber = int(input('Введи номер светодиода: '))
blinkCount = int(input('Количество миганий: '))
blinkPeriod = float(input('Интервал: '))
blink(ledNumber, blinkCount, blinkPeriod)
 