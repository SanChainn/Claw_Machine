import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


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
