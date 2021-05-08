import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
N = [24,25,8,7,12,16,20,21]
GPIO.setup(N, GPIO.OUT)

GPIO_PWM_0 = 12
GPIO_PWM_1 = 13
WORK_TIME = 10
DUTY_CYCLE = 50
FREQUENCY = 100

pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
pwmOutput_1 = GPIO.PWM(GPIO_PWM_1, 2 * FREQUENCY)
pwmOutput_0.start(DUTY_CYCLE)
pwmOutput_1.start(DUTY_CYCLE)
time.sleep(WORK_TIME)

pwmOutput_0.stop()
pwmOutput_1.stop()

GPIO.cleanup()