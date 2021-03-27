import RPi.GPIO as GPIO
import time 


GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

D=[21,20,16,12,1,7,8,25]

for i in D:
	GPIO.output(i,1)
	time.sleep(0,5)
for i in D:
	GPIO.output(i,0)
	time.sleep(0,5)