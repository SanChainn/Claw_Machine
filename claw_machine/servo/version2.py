import RPi.GPIO as GPIO
import time

servoPIN = 17    #4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.0) # Initialization
print("DutyCycle : 2.0 and angle 0")
try:
  while True:
    
    x = input("")
    p.ChangeDutyCycle(5.8)
    print("DutyCycle : 5.8 and angle 50")
    #time.sleep(0.5)


    
    x = input("")
    p.ChangeDutyCycle(2.0)
    print("DutyCycle :2.0 and angle 0")
   # time.sleep(0.5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
