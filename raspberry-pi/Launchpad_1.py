# type: ignore
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT 

Count_time = 11
 
while True:
    if Count_time >= 1:
        Count_time = Count_time - 1
        time.sleep(1)
        print(Count_time)
        if Count_time == 0:
            print("Launch")