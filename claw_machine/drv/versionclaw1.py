from time import sleep
import pigpio
import sys
import serial
import RPi.GPIO as GPIO

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()



DIR_X = 20     # Direction GPIO Pin
STEP_X = 21    # Step GPIO Pin
#SWITCH =   # GPIO pin of switch


DIR_Y = 16
STEP_Y= 12


DIR_Z =7
STEP_Z= 15

# Connect to pigpiod daemon
pi_x = pigpio.pi()
pi_y = pigpio.pi()
pi_z = pigpio.pi()


# Set up pins as an output
pi_x.set_mode(DIR_X, pigpio.OUTPUT)
pi_x.set_mode(STEP_X, pigpio.OUTPUT)

# Set up pins as an output
pi_y.set_mode(DIR_Y, pigpio.OUTPUT)
pi_y.set_mode(STEP_Y, pigpio.OUTPUT)


# Set up pins as an output
pi_z.set_mode(DIR_Z, pigpio.OUTPUT)
pi_z.set_mode(STEP_Z, pigpio.OUTPUT)




# Set up input switch
#pi_x.set_mode(SWITCH, pigpio.INPUT)
#pi_x.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (18, 23, 24)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi_x.write(MODE[i], RESOLUTION['Full'][i])

# Set duty cycle and frequency
pi_x.set_PWM_dutycycle(STEP_X, 200)  # PWM 1/2 On 1/2 Off
pi_x.set_PWM_frequency(STEP_X, 1250)  # 500 pulses per second

# Set duty cycle and frequency
pi_y.set_PWM_dutycycle(STEP_Y, 200)  # PWM 1/2 On 1/2 Off
pi_y.set_PWM_frequency(STEP_Y, 1250)  # 500 pulses per second

# Set duty cycle and frequency
pi_z.set_PWM_dutycycle(STEP_Y, 200)  # PWM 1/2 On 1/2 Off
pi_z.set_PWM_frequency(STEP_Y, 1250)  # 500 pulses per second


#dir_x = sys.argv[1]
#dir_y = sys.argv[2]


def move_x():
        pi_x.set_PWM_dutycycle(STEP_X, 128)  # PWM 1/2 On 1/2 Off
        pi_x.set_PWM_frequency(STEP_X, 1250)


def move_y():
        pi_y.set_PWM_dutycycle(STEP_Y, 128)  # PWM 1/2 On 1/2 Off
        pi_y.set_PWM_frequency(STEP_Y, 1250)


def move_z():
	pi_z.set_PWM_dutycycle(STEP_Z,128)
	pi_z.set_PWM_frequency(STEP_Z,1250)


def stop_x():
        pi_x.set_PWM_dutycycle(STEP_X,0)
        pi_x.set_PWM_frequency(STEP_X,0)


def stop_y():
        pi_y.set_PWM_dutycycle(STEP_Y,0)
        pi_y.set_PWM_frequency(STEP_Y,0)


def stop_z():
        pi_z.set_PWM_dutycycle(STEP_Z,0)
        pi_z.set_PWM_frequency(STEP_Z,0)	

try:
    while True:
        #pi.write(DIR,int(sys.argv[1]))  # Set direction
	#if dir_x == 'forward':
	#	pi.write(DIR,0)
	#	print("Moving Forward")
	#else:
	#	pi.write(DIR,1)
	#	print("Moving Backward")
        #sleep(.1)
	
	pi_x.write(DIR_X,0)
	pi_y.write(DIR_Y,0)
	move_y()
	move_x()
	sleep(1)
	



except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    #pi_x.set_PWM_dutycycle(STEP_X, 0)  # PWM off
    #pi_x.stop()

   stop_x()
   stop_y()
