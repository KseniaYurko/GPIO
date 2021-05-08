import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
с
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
 
GPIO.cleanup()