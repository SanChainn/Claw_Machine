import serial
import time

def Read_Weight():
        time.sleep(2)

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

        while 1:

                for i in range(10):
                        data = ser.readline()
                        print(data)
#                       Serial.flush();
                Serial.flush();


Read_Weight()
