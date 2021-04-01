import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)

def closeAll(all):
    for i in range (8):
        board.digital[N[i]].write(0)
closeAll(all)
