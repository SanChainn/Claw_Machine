import RPi.GPIO as GPIO
import seven as se
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

def dig_off(x):
	GPIO.output(digits[x],0)


seg =[se.zero(segments),se.onee(segments),se.two(segments),se.three(segments),se.four(segments),se.five(segments),se.six(segments),se.seven(segments),se.eight(segments),se.nine(segments)]


dig_off(1)
dig_off(2)
dig_off(3)



print(seg)
