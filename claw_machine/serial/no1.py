import serial
import time

ser = serial.Serial(
                    port='/dev/ttyACM0',
                    baudrate = 115200,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    xonxoff = False,
                    rtscts = False,
                    dsrdtr = False,
                    timeout = 1
                     )
while True:	
	data = ser.readline()
	print(data)
