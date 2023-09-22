# type: ignore
import time
import board
import digitalio

Gled = digitalio.DigitalInOut(board.GP0) #Sets LED pin
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2) #Sets LED pin
Rled.direction = digitalio.Direction.OUTPUT 

Count_time = 11     #creates a variable 
 
while True:
    if Count_time >= 1: #is it launched?
        Count_time = Count_time - 1 #count
        Rled.value = True   #LED blink
        time.sleep(.5)      #.5 second delay
        Rled.value = False
        time.sleep(.5)      #.5 second delay
        print(Count_time)   #LED blink
        if Count_time == 0: #Count over?
            print("Launch")
            GlAed.value = True  #turn Green LED on
            Rled.value = False  #Turn Red LED off
