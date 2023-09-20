# type: ignore
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED) #Sets LED pin
led.direction = digitalio.Direction.OUTPUT 

while True:
    led.value = True    #LED on
    time.sleep(1)       #Time delay for LED
    led.value = False   #LED off
    time.sleep(1)