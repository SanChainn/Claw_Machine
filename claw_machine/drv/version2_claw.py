from time import sleep
import pigpio
import sys
import serial


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()



DIR_X = 20     # Direction GPIO Pin
STEP_X = 21    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi_x = pigpio.pi()
pi_y = pigpio.pi()

# Set up pins as an output
pi_x.set_mode(DIR_X, pigpio.OUTPUT)
pi_x.set_mode(STEP_X, pigpio.OUTPUT)

# Set up input switch
pi_x.set_mode(SWITCH, pigpio.INPUT)
pi_x.set_pull_up_down(SWITCH, pigpio.PUD_UP)

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

#dir_x = sys.argv[1]
#dir_y = sys.argv[2]


def move_x():
        pi_x.set_PWM_dutycycle(STEP_X, 128)  # PWM 1/2 On 1/2 Off
        pi_x.set_PWM_frequency(STEP_X, 1250)




def stop_x():
        pi_x.set_PWM_dutycycle(STEP_X,0)
        pi_x.set_PWM_frequency(STEP_X,0)



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
	
	#pi_x.write(DIR_X,0)
	#move_x()
	#sleep(1)
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
		line = int(line)
		print(line)
		if line > 480 and line < 600:
			stop_x()
			print("STOP")
		elif line < 480 :
			pi_x.write(DIR_X,0)
			move_x()
			#sleep(0.1)
			print("MOVING left >>")
		elif line > 600 :
                        pi_x.write(DIR_X,1)
                        move_x()
                        #sleep(0.1)
                        print("MOVING Right >>")


except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi_x.set_PWM_dutycycle(STEP_X, 0)  # PWM off
    pi_x.stop()
