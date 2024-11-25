import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ir=16
led=4
GPIO.setup(ir,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

while True:
	ir_state=GPIO.input(ir)
	if ir_state==0:
		GPIO.output(led,GPIO.HIGH)
		print("LED is on")
	else:
		GPIO.output(led,GPIO.LOW)
		print("LED is off")
	sleep(1)