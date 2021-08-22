import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




def zero(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],1)
def onee(segments):
        GPIO.output(segments[0],1)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],1)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],1)

def two(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],1)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],0)
def three(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],0)


def four(segments):
        GPIO.output(segments[0],1)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],1)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def five(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],1)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def six(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],1)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def seven(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],1)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],1)
        GPIO.output(segments[6],1)

def eight(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],0)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)

def nine(segments):
        GPIO.output(segments[0],0)
        GPIO.output(segments[1],0)
        GPIO.output(segments[2],0)
        GPIO.output(segments[3],0)
        GPIO.output(segments[4],1)
        GPIO.output(segments[5],0)
        GPIO.output(segments[6],0)
