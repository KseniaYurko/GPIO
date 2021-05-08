import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)

def lightNumber(number):
    a = bin(decNumber)
    b = a[2::]
    print(b)
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
    for i in range (len(number)):
        if number[i] == '0':
            GPIO.output(N[ledNumber],0)
        elif number[i] == '1':
            GPIO.output(N[ledNumber],1)
decNumber = int(input('Введите число от 0 до 255: '))
lightNumber(decNumber) 