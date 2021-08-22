#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=18, DIO=15, brightness=1.0)

# Basic Display Update:
digits = [1, 2, 3, 4]
Display.Show(digits)
print "1234  - Working? (Press Key)"
scrap = raw_input()

#Display.Clear()
num = [0,1,2,3,4,5,6]


Display.Clear()
Display.Show1(2,6)
Display.Show1(3,0)
#sleep(1)

#Display.Clear()
sleep(1)

count = 6
for i in range(60,0,-1):
	print(i)
	Display.Show1(3, i%10)
        sleep(0.1)
        print(i%10)
	if i%10 == 0:
	    	count = count -1
		print(count)
		Display.Show1(2,num[count])
		print("NNN")

Display.Show1(3,0)
Display.Show1(2,0)     	

print("Enter  ")
ss = raw_input()
Display.Show1(0,1)
Display.Show1(1,0)
Display.Show1(2,0)
Display.Show1(3,0)

Display.Clear()
while True:
	count = int(raw_input("Enter count :"))
	Display.Show1(1,count)
	Display.Show1(2,0)
	Display.Show1(3,0)






print('done.')
Display.cleanup()
