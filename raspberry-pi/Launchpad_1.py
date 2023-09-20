# type: ignore
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP1) #Sets LED pin
led.direction = digitalio.Direction.OUTPUT 

Count_time = 11 #creates a variable 
 
while True:
    if Count_time >= 1: #is it launched?
        Count_time = Count_time - 1 #count
        time.sleep(1)   #1 second delay
        print(Count_time)
        if Count_time == 0: #Count over
            print("Launch") #prints launch
            