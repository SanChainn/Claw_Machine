import serial
from time import sleep

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
	    #line = ser.readline().rstrip()
	    line = str(line)
	    #print(line)
	    leng = len(line)
	    if line[leng-1] is 'x':
		x = line.split('x')
		x =int(x[0])
		print("Xvalue : ",x , type(x))
	    else:
		y = line.split('y')
		y = int(y[0])
		print("Yvalue : ",y , type(y))
	    #sleep(0.2)
	
	    	
