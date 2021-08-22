import RPi.GPIO as GPIO
import time

glue_sensor = 9
stamp_sensor = 19
buzzer = 19



GPIO.setmode(GPIO.BCM)
GPIO.setup(glue_sensor,GPIO.IN)
GPIO.setup(stamp_sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print("IR Sensors are  Ready.....")
print(" ")

try: 
   while True:
      if GPIO.input(glue_sensor):
          GPIO.output(buzzer,False)
          print("Glue_Sensor Object not Detected")
	  time.sleep(0.003)
      elif GPIO.input(glue_sensor)==False:
           GPIO.output(buzzer,True)
	   print("Glue_Sensor Object  Detected ")
	   time.sleep(0.003)
#      if GPIO.input(stamp_sensor):
#	   GPIO.output(buzzer,False)
#	   print("Stamp_Sensor Object not Detected")
#	   time.sleep(0.003)
#      elif GPIO.input(stamp_sensor)==False:
#	    GPIO.output(buzzer,True)
#	    print("Stamp_Sensor Object Detected")
# 	    time.sleep(0.003)

except KeyboardInterrupt:
    GPIO.cleanup()
