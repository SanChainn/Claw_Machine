from gpiozero import Button
from time import sleep

button1 =Button(0)
button2 =Button(11)

while True:
	if button1.is_pressed:
		print("Button1 is pressed")
		sleep(0.2)
	else:
		print("Button1 is not pressed")
		#sleep(0.2)

	if button2.is_pressed:
		print("Button2 is pressed")
		sleep(0.2)
	else:
		print("Button2 is not pressed")
		#sleep(0.2)
	if button1.is_pressed and button2.is_pressed:
		print("Both buttons are pressed")
