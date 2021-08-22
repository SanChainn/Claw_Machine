import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


digits = (23,24,17,27)

for digit in digits:
	GPIO.setup(digit,GPIO.OUT)
	sleep(1)
	GPIO.output(digit,1)



def off():
	for a in range(4):
		GPIO.output(digits[a],0)
		sleep(1)

def on():
	for a in range(4):
		GPIO.output(digits[a],1)
		sleep(1)


for a in range(10):
	off()
	sleep(1)
	on()
	sleep(1)
