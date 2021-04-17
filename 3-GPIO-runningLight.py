import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
N = [21,20,16,12,7,8,25,24]
GPIO.setup(N, GPIO.OUT)

def runningLight(count, period):
    ledNumber = int(input('С какого светодиода начинать? '))
    LED = ledNumber-1
    for i in range(count):
        GPIO.output(N[LED],1)
        time.sleep(period)
        GPIO.output(N[LED],0)
        if LED <= 7:
            LED = LED+1
        elif LED == 8:
            LED = LED-8
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningLight(count, period)

GPIO.output(N, 0)
GPIO.cleanup()