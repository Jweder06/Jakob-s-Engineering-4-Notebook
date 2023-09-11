# type: ignore
import time
import board
import digitalio

Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2)
Rled.direction = digitalio.Direction.OUTPUT 
Button = digitalio.DigitalInOut(board.GP1)
Button.direction = digitalio.Direction.INPUT 
Count_time = 11
 
while True:
print(button.value)