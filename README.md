# Engineering_4_Notebook


## Led Blink

### Assignment Description
This Assignment was a part of the pico introduction. It was a simple assignment to get us used to the Raspberry Pi and the Python language. The assignment was to make an LED blink on and off.

### Evidence



### Code
```python
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
```
### Video
### Reflection 
For me this assignment was a very basic introduction back into VS code. I learned how to operate a pico and how to edit and save the code on the pico. I also learned how to find a pinmap of the pic itself.

## Launchpad 1 

### Assignment Description
In this assignment we where tasked with making a countdown timer, counting down from 10 to 0, with a interval of 1 second after wich we would print "launch".

### Evidence


### Code
```python
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
```            

### Reflection
This assignment was also a introductory one that taught us how to activate a LED by controlling a pin. It uses the previous code as a base and taught me how to add more complexity into my original code. I also learned how to properly restart my code and how to reset the pico when the code was finished.

## Launchpad 2 


### Assignment Description
In this assignment we where tasked with creating a countdowntime but one that signaled the countdown with an LED. The LED would blink once every second and when the countdown reached 0 another LED would turn on.
### Evidence
### Code
```python
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
```
### Wiring
## Launchpad 3 
 
### Assignment Description
I did the "spicy" version of this assignment this entailed me to make a system that "aborted" the launch on the second button press. This would then reset the countdown to the original state of waiting for the first button press.
### Evidence
### Code
```python
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
```
### Wiring
## Launchpad 4  
### Assignment Description
### Evidence
### Code
```python
# type: ignore
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

Gled = digitalio.DigitalInOut(board.GP0)    #Sets LED pin
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2)    #Sets LED pin
Rled.direction = digitalio.Direction.OUTPUT 
Button = digitalio.DigitalInOut(board.GP1)  #Sets Button pin
Button.pull = digitalio.Pull.DOWN   #Sets Pulldown
pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
Count_time = 11 #creates a variables for button, counter and debounce  
Button_state = 0
Start_value = 0
while True:
     if Button.value == True and Button_state == 0:  #button debounce
         Button_state = 1
         Start_value = Start_value + 1
     if Button.value == False:  #button debounce
         Button_state = 0
     if Count_time >= 1 and Start_value == 1: #Previous Count code with servo
          Gled.value = False
          Count_time = Count_time - 1
          Rled.value = True
          time.sleep(.5)
          Rled.value = False
          time.sleep(.5)
          print(Count_time)
          servo1.angle = 180
     if Count_time == 0 and Start_value == 1: #Previous Launch code with servo
          print("Launch")
          Gled.value = True
          Rled.value = False
          time.sleep(2)
          servo1.angle = 0  #Reset Servo
     if   Start_value == 2:
         print("abort")
     if Start_value == 3:
         Start_value = 1
         Count_time = 11
```
### Wiring

## Crash Avoidance Part 1
### Assignment Description
### Evidence


### Code
```python

```
### Wiring
