import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

N = [21,20,16,12,7,8,25,24]
GPIO.setup(N, GPIO.OUT)
GPIO.output(N, 0)

def lightUp(ledNumber, period):
    GPIO.output(N[ledNumber-1],1)
    time.sleep(period)
    GPIO.output(N[ledNumber-1],0)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)

GPIO.output(N, 0)
GPIO.cleanup()