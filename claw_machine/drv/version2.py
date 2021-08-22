from time import sleep
import pigpio
import sys

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (18, 23, 24)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Full'][i])

# Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP, 200)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP, 1250)  # 500 pulses per second

dir_x = sys.argv[1]
#dir_y = sys.argv[2]

try:
    while True:
        #pi.write(DIR,int(sys.argv[1]))  # Set direction
	if dir_x == 'forward':
		pi.write(DIR,0)
		print("Moving Forward")
	else:
		pi.write(DIR,1)
		print("Moving Backward")
        sleep(1)

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.stop()
