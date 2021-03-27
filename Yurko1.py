import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N,GPIO.OUT)

def lightUp(ledNumber,period):
    GPIO.output(N[ledNumber],1)
    time.sleep(period)
    GPIO.output(N[ledNumber],0)

#lightUp(2,1)



def blink(ledNumber, blinkCount, blinkPeriod):
    
    for i in range (blinkCount):
        GPIO.output(N[ledNumber],1)
        time.sleep(blinkPeriod)
        GPIO.output(N[ledNumber],0)
        time.sleep(blinkPeriod)
#blink(4,4,1)


def runningLight(count, period):
    ledNumber = 0
    for i in range (count):
        s = N[ledNumber]
        lightUp()
        s = N[ledNumber]+1
runningLight(5,1)

GPIO.output(N,0)
GPIO.cleanup()