import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
N = [21,20,16,12,7,8,25,24]
GPIO.setup(N, GPIO.OUT)

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
DarkALL()