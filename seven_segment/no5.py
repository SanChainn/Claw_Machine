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
def off():
        for a in range(4):
                GPIO.output(digits[a],0)
                sleep(0.3)

def on():
        for a in range(4):
                GPIO.output(digits[a],1)
                sleep(0.3)

#for a in range(0,7):
#	GPIO.output(segments[a],1)
#	sleep(0.5)

#for a in range(0,7):
#	GPIO.output(segments[a],0)
#	sleep(0.5)




def zero():
	GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],0)
	GPIO.output(segments[6],1)
        


def onee():
	GPIO.output(segments[0],1)
	GPIO.output(segments[1],0)
	GPIO.output(segments[2],0)
        GPIO.output(segments[3],1)
	GPIO.output(segments[4],1)
        GPIO.output(segments[5],1)
	GPIO.output(segments[6],1)

def two():
	GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],1)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],0)

def three():
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],0)


def four():
        GPIO.output(segments[0],1)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],1)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def five():
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],1)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def six():
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],1)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def seven():
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],1)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],1)

def eight():
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def nine():
	GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)


while True:
	zero()
	sleep(0.3)
	onee()
	sleep(0.3)
	two()
	sleep(0.3)
	three()
	sleep(0.3)
	four()
        sleep(0.3)
        five()
        sleep(0.3)
        six()
        sleep(0.3)
	seven()
        sleep(0.3)
        eight()
        sleep(0.3)
        nine()
        sleep(0.3)


number = [zero(),onee()]


print(number[0])

while True:
	number[0]
	sleep(1)
	number[1]
	sleep(1)
