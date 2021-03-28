import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def decToBinNumber(decNumber):
    a = bin(decNumber)
    b = a[2::]
    print(b)
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
decNumber = int(input('Введите число от 0 до 255: '))
decToBinNumber(decNumber) 