# type: ignore
import time
import board
import digitalio

Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2)
Rled.direction = digitalio.Direction.OUTPUT 

Count_time = 11
 
while True:
    if Count_time >= 1:
        Count_time = Count_time - 1
        Rled.value = True
        time.sleep(.5)
        Rled.value = False
        time.sleep(.5)
        print(Count_time)
        if Count_time == 0:
            print("Launch")
            Gled.value = True
            Rled.value = False
