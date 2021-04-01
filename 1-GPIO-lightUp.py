import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)


def lightUp(ledNumber, period):
    GPIO.output(N[ledNumber],1)
    time.sleep(period)
    GPIO.output(N[ledNumber],0)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)
