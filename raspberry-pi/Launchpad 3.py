# type: ignore
import time
import board
import digitalio

Gled = digitalio.DigitalInOut(board.GP0)    #Sets LED pin
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2)    #Sets LED pin
Rled.direction = digitalio.Direction.OUTPUT 
Button = digitalio.DigitalInOut(board.GP1)  #Sets Button pin
Button.pull = digitalio.Pull.DOWN   #Sets Pulldown
Count_time = 11 #creates a variables for button, counter and debounce  
Button_state = 0
Start_value = 0
while True:
    if Button.value == True and Button_state == 0:  #button debounce
        Button_state = 1
        Start_value = Start_value + 1
    if Button.value == False:  #button debounce
        Button_state = 0
    if Count_time >= 1 and Start_value == 1: #Previous Count code
         Gled.value = False
         Count_time = Count_time - 1
         Rled.value = True
         time.sleep(.5)
         Rled.value = False
         time.sleep(.5)
         print(Count_time)
    if Count_time == 0: #Previous Launch code
         print("Launch")
         Gled.value = True
         Rled.value = False
         time.sleep(5)
    if   Start_value == 2: # Abort detection
        print("abort")
    if Start_value == 3:
        Start_value = 1 #Reset Abort Status
        Count_time = 11 #Reset Count