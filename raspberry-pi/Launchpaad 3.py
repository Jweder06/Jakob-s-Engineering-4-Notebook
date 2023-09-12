# type: ignore
import time
import board
import digitalio

Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2)
Rled.direction = digitalio.Direction.OUTPUT 
Button = digitalio.DigitalInOut(board.GP1)
Button.pull = digitalio.Pull.DOWN
Count_time = 11
Button_state = 0
while True:
    if Button.value == True and Button_state == 0:
        print(Button_state)
        Button_state = 1
    elif Button.value == False:
        Button_state = 0
    if Count_time >= 1 and Button_state == 1:
        Gled.value = False
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
        time.sleep(5)
        Count_time = 11