import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

btn=16
led=4
GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

while True:
	button_state=GPIO.input(btn)
	print(button_state)
	if button_state==0:
		GPIO.output(led,GPIO.HIGH)
		print("LED is on")
	else:
		GPIO.output(led,GPIO.LOW)
		print("LED is off")
	sleep(1)