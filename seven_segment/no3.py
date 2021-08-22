import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


digits = (23,24,17,27)

for digit in digits:
	GPIO.setup(digit,GPIO.OUT)
	sleep(1)
	GPIO.output(digit,1)


segments = (7,8,18,20,21,26,16)
for seg in segments:
	GPIO.setup(seg,GPIO.OUT)
	GPIO.output(seg,0)


num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}





def off():
	for a in range(4):
		GPIO.output(digits[a],0)
		sleep(0.3)

def on():
	for a in range(4):
		GPIO.output(digits[a],1)
		sleep(0.3)


#for a in range(1):
#	off()
#	on()



#while True:
#	for digit in range(4):
#		for loop in range(0,7):
#			digit = str(digit)
#			GPIO.output(segments[loop],num[digit][loop])
#			sleep(1)

off()

GPIO.output(digits[0],1)


while True:
	for a in range(0,7):
		GPIO.output(segments[a],num['1'][a])
		sleep(0.5)
