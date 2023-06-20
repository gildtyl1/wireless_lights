import bluetooth
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
fpin = 14
GPIO.setup(fpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("98:D3:41:F6:B3:94", 1))

while True:
#	message = "hello"
#	sock.send(message)
#	time.sleep(1)

#sock.close()
	switch_state = GPIO.input(fpin)

	if switch_state == False:
		sock.send("1")
		message = "1"
		sock.sendall(message.encode())
		print("on")
		time.sleep(1)
	if switch_state == True:
		sock.send("0")
		message = "0"
		sock.sendall(message.encode())
		print("off")
		time.sleep(1)
sock.close()
