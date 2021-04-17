import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
N = [21,20,16,12,7,8,25,24]
GPIO.setup(N, GPIO.OUT)

def LightALL():
    for i in range(8):
        GPIO.output(N[i], 1)

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)

LightALL()
time.sleep(6)
DarkALL()