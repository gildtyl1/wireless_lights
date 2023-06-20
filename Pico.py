from machine import UART, Pin
rxData = bytes()
uart1 = UART(0,baudrate = 9600,tx = Pin(0),rx=Pin(1))
led = machine.Pin(10, machine.Pin.OUT)
led.value(0)
while True:
    if uart1.any()>0:
        rxData = uart1.read(1)
        if "1" in rxData:
            print("Turning ON")
            led.value(1)
        elif "0" in rxData:
            print("Turning OFF")
            led.value(0)
