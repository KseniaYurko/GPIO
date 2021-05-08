import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
N = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(N, GPIO.OUT)

def runningLight(count, period):
    ledNumber = int(input('С какого светодиода начинать? '))
    LED = ledNumber-1
    for i in range(count):
        GPIO.output(N[LED],1)
        time.sleep(period)
        GPIO.output(N[LED],0)
        if LED <= 6:
            LED = LED+1
        elif LED == 7:
            LED = LED-7
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningLight(count, period)

GPIO.output(N, 0)
GPIO.cleanup()