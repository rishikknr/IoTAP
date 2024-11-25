import RPi.GPIO as GPIO
from time import sleep
from w1thermsensor import W1ThermSensor

s=W1ThermSensor()
GPIO.setmode(GPIO.BCM)
tempPin=4
GPIO.setup(tempPin,GPIO.IN)

while True:
	temp=s.get_temperature()
	print(f"The temperature is: {temp}")
	sleep(1)