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

```
### Wiring
## Launchpad 3 
 
### Assignment Description
I did the "spicy" version of this assignment this entailed me to make a system that "aborted" the launch on the second button press. This would then reset the countdown to the original state of waiting for the first button press.
### Evidence
### Code
```python

```
### Wiring
## Launchpad 4  
### Assignment Description
### Evidence
### Code
```python

```
### Wiring

## Crash Avoidance Part 1
### Assignment Description
### Evidence
### Code
```python

```
### Wiring
