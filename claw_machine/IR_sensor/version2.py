import RPi.GPIO as GPIO
import time

glue_sensor = 26
stamp_sensor = 13
buzzer = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(glue_sensor,GPIO.IN)
GPIO.setup(stamp_sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
delay=0.3
GPIO.output(buzzer,False)
print("IR Sensors are  Ready.....")
print(" ")

try: 
   while True:
      if GPIO.input(glue_sensor):
          GPIO.output(buzzer,False)
          print("Glue_Sensor Object not Detected")
	  time.sleep(delay)
      if GPIO.input(glue_sensor)==False:
           GPIO.output(buzzer,True)
	   print("Glue_Sensor Object  Detected ")
	   time.sleep(delay)
      if GPIO.input(stamp_sensor):
	   GPIO.output(buzzer,False)
	   print("Stamp_Sensor Object not Detected")
	   time.sleep(delay)
      if GPIO.input(stamp_sensor)==False:
	    GPIO.output(buzzer,True)
	    print("Stamp_Sensor Object Detected")
 	    time.sleep(delay)

except KeyboardInterrupt:
    GPIO.cleanup()
