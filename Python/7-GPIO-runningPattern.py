import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)

def closeAll(all):
    for i in range (8):
        GPIO.output(N[ledNumber],0)
closeAll(all)


def runningPattern(pattern, direction):
    a = bin(pattern)
    b = a[2::]
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
    if direction == 1:
        for i in range(count):
            number.insert(0, number[7])
            number.pop(8)
            for i in range (8):
                if number[i] == '0':
                    GPIO.output(N[i],0)
                elif number[i] == '1':
                    GPIO.output(N[i],1)
            time.sleep(period)
    elif direction == 0:
        for i in range(count):
            number.insert(8, number[0])
            number.pop(0)
            for i in range (8):
                if number[i] == '0':
                    GPIO.output(N[i],0)
                elif number[i] == '1':
                    GPIO.output(N[i],1)
            time.sleep(period)

pattern = int(input('Введите число от 0 до 255: '))
count = int(input('Сколько раз передвинуть? '))
period = float(input('Интервал: '))
direction = int(input('В какую сторону? (1-вправо; 0-влево) '))
runningPattern(pattern, direction)
closeAll(all)

