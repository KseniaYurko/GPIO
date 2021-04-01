import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)

def runningLight(count, period):
    for i in range(count):
        GPIO.output(N[ledNumber],1)
        time.sleep(period)
        GPIO.output(N[ledNumber],0)
        if N[ledNumber]<9:
            N[ledNumber]=N[ledNumber]+1
        elif N[ledNumber]>=9:
            N[ledNumber]=N[ledNumber]-7
ledNumber = int(input('С какого светодиода начинать? '))
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningLight(count, period)