import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
led=18 #GPIO pin
GPIO.setup(led,GPIO.OUT)

while True:
    GPIO.output(led,GPIO.HIGH)
    print("LED is on")
    sleep(1)
    GPIO.output(led,GPIO.LOW)
    print("LED is off")
    sleep(1)