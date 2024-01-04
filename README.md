# Engineering_4_Notebook


## Led Blink

### Assignment Description
This Assignment was a part of the pico introduction. It was a simple assignment to get us used to the Raspberry Pi and the Python language. The assignment was to make an LED blink on and off.

## Evidence
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
<img src="images\Countdown LP1.gif" width="500">

### Reflection 
For me this assignment was a very basic introduction back into VS code. I learned how to operate a pico and how to edit and save the code on the pico. I also learned how to find a pinmap of the pic itself.

# Launchpad 1 

### Assignment Description
In this assignment we where tasked with making a countdown timer, counting down from 10 to 0, with a interval of 1 second after wich we would print "launch".

## Evidence


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
### Video
<img src="images\Countdown LP1.gif" width="500">

### Reflection

This assignment was also a introductory one that taught us how to activate a LED by controlling a pin. It uses the previous code as a base and taught me how to add more complexity into my original code. I also learned how to properly restart my code and how to reset the pico when the code was finished.


# Launchpad 2 
### Assignment Description
In this assignment we where tasked with creating a countdowntime but one that signaled the countdown with an LED. The LED would blink once every second and when the countdown reached 0 another LED would turn on.
## Evidence
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

<img src="images\Launchpad 2.png" width="500">

### Video
<img src="images\LP2.gif" width="500">

### Reflection
This assignment was another introductory one but was also important for me to relearn the basics of wiring and powering an LED. It also taught me how to pull up a pin map and what each pin is for on the Pico. The most important thing that I took away from this assignment was reintroducing the basics of coding for example in the beginning I forgot to properly space my if statements in my while true and even asked for help for such a basic mistake.



# Launchpad 3 
 
### Assignment Description
I did the "spicy" version of this assignment this entailed me to make a system that "aborted" the launch on the second button press. This would then reset the countdown to the original state of waiting for the first button press.
## Evidence
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
<img src="images\launchpad 3.png" width="500">

### Video
<img src="images\Ez gif LP3.gif" width="500">

### Reflection
This assignment was also building on the previous set of code and continued to reteach me the things I had forgotten throughout the summer. For this assignment, I debounced a button something that I had done a lot in my project from last year but had totally forgotten how to do it. The main problems I had were figuring out how to properly debounce and I was accidentally shorting my LED circuit because my resistors were touching. My main takeaways from this assignment were again relearning the basics but also to double check my wiring.





# Launchpad 4  
### Assignment Description
In this assignment, we had to build on the previous code and add a Servo that once the launch counter had reached zero we had to retract the” launch arm” and make sure all the previous systems still worked.
## Evidence
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
<img src="images\Launchpad 4.png" width="500">

### Video
<img src="images\LP4.gif" width="500">

### Reflection
In this assignment, we used the previous code to control a servo that would activate once the launch counter was finished again building on our previous code. Each assignment was progressively adding more capability to our Pico and each system was its own sort of module. This is a very valuable lesson I can take away on building not just code but  General systems within my projects modularly adding new capabilities and making my system more redundant. This assignment also taught me how to add libraries to my Pico something I had to relearn from last year.


# Crash Avoidance Part 1
### Assignment Description
Integrate an MPU6050 accelerometer with a  Pico using I2C communication. Wire the MPU6050 to the Pico, read acceleration values in m/s² for x, y, and z axes, and display them on the serial monitor.
## Evidence

### Code
```python
# type: ignore
import adafruit_mpu6050 #import Variables
import busio
import board                                   
import time
import digitalio

led = digitalio.DigitalInOut(board.GP0) #sets LED pin
led.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14    #sets SDA and SCL
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    led.value = False
    print(mpu.acceleration) #Print acceleration
    while mpu.acceleration[2] < 0.95: #Checkes acceleration for LED
        led.value = True    #Turn LED off
        print(mpu.acceleration) 
```
### Wiring
<img src="images\Crash Avoindance 1.png" width="500">

### Video
<img src="images\Acel 1.gif" width="500">

### Reflection
For this assignment but most difficult part was definitely figuring out how the accelerometer actually worked “which way does this thing go”.The most interesting part was definitely the SDA and SCL pins which allowed us to communicate with our accelerometer.Otherwise it was the standard hook up a sensor and  test it by printing it into the serial monitor again teaching us modularity of our code.



# Crash Avoidance Part 2
### Assignment Description
We designed a crash avoidance module for a scout helicopter mission using a Pico. We incorporated a tilt sensor to activate an LED warning light when the helicopter tilted 90 degrees. The Pico was configured to run independently using a JST Battery power source.
## Evidence

### Wiring
<img src="images\ACEL 2 wire.png" width="500">

### Video
<img src="images\Acel 2.gif" width="500">

### Reflection
For this assignment I thought it would be relatively simple but how wrong I was.  I had wired everything up according to the instructions but my Pico would connect even though it had been working the day before.I tried switching out  connection cabling checking my power and ground pins to make sure I wasn't shorting  and everything checked out except for every time the board was plugged in the connection part would immediately get burning hot which is not a good sign. After looking for the short for almost the entire class  I decided to switch up my breadboard and rip  off the back adhesive exposing the wire connections and behold a short between my ground and power pins which luckily hadn't fried my Pico. 
<img src="images\Breadboard.png" width="500">

# Crash Avoidance Part 3
### Assignment Description
In this assignment we added onto our previous code and added a OLED display to display your accelerometer values. It was connected to the PICO using the SDA and SCL port.
## Evidence
### Code
```python
# type: ignore
import adafruit_mpu6050 #import libraries
import busio
import board                                   
import time
import digitalio
from adafruit_display_text import label #import from folder
import adafruit_displayio_ssd1306
import terminalio
import displayio
displayio.release_displays()


led = digitalio.DigitalInOut(board.GP0) #sets LED pin
led.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14    #sets SDA and SCL
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)   #sets adress for accelerometer

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP5)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY" 
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)  # the order of this command is (font, text, text color, and location)
splash.append(text_area)    

# send display group to screen
display.show(splash)
while True:
    led.value = False
    print(mpu.acceleration) #Print acceleration
    text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}"       #tell the LCD the format of the aceleration text
    while mpu.acceleration[2] < 0.95: #Checkes acceleration for LED
        led.value = True    #Turn LED off
        print(mpu.acceleration) 
        text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}"   #tell the LCD the format of the aceleration text
```
### The Holy Grail of Wiring
<img src="images\ACEL 3 wire.png" width="500">

<img src="images\The holy grail.JPG" width="500">

### Video
<img src="images\Acel3.gif" width="500">

### Reflection
After the disaster that was the last assignment I hope to get off on a better start. this started with stubbornly refusing to read the instructions and asking a bunch of stupid questions (sorry Mr miller). Afterwards it was a smooth ride reading and following instructions to set up the accelerometer to print onto the OLED display. The most interesting and most difficult part was definitely getting the I2C addresses and plugging them into the code. 


# Onshape(FDA)

# FEA_Part_1_(Beam_Design)

### Assignment Description

A beam must stick straight out from a predetermined platform, and the beam gets a bucket screwed into the side of it, then weight gets added. You need to maximize the ammount of weight that that bucket can hold. This is constrained by these contraints:
* The beam must use the provided attachment block with no modifications
* The beam with the attachment block must be able to fully engage with the holder
* The beam must use the example eye bolt mounting geometry
* The center of the eyebolt hole must be 180 mm from the front face of the attachment block (in a direction perpendicular to the front face)
* No part of the beam may extend below the bottom face of the attachment block
* All vertical angles must be >= 45° measured relative to the horizontal plane (no overhangs)
* The beam must be PLA material
* The entire beam, including attachment block, must weight <= 13 grams

### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/92a40a9416b5315e6a429686/w/2b2c3d00de9869597b85e9c4/e/d26c7202e8ba614aecbc70b2)

### Part Image

<img src="images\FDA p1.png" width="500">

### Reflection

For this assignment, three things went wrong:
* The weight of the object was way too large, so we took advantage of the fact that the nozel is 0.04mm. We removed a 0.03mm layer so that the computer would think that it weighs less than it actually does.
* We had too much weight again, so this time we filleted the edges down.
* Originally, the document was unable to be copyed, so we spent a portion of the first class trying to export the object and import it into our own doc which eventually failed because STEP files dont save individual parts, so we couldnt accuratly measure weight.

# FEA Part 3 (Analysis)

### Assignment Description
For this assignment we were instructed to take our previous part and use FDA to analyse the stress on our part. We Examined the beams we just created in Onshape, and try to optimize the beam in two ways. Our goal was to minimize beam bending while maximizing the mass the beam can support before failing.
### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/92a40a9416b5315e6a429686/w/2b2c3d00de9869597b85e9c4/e/d26c7202e8ba614aecbc70b2)

### Part Image
<img src="images\FDA p3.png" width="500">

<img src="images\FDA image.png" width="500">

### Reflection
The FDA simulation forced us to make a big decision fix our curent design or scrap it and start over with the new information we learned. We decided to do both and redesign the previous part in a new part studio with some new additions. This proved to be the most efective path as we where much faster in creating the new part but had a mush better outcome.

# FEA_Part_4_(Iterative_Design)

### Assignment Description

After simulation, you should have an idea of where your beam needs to improve. Now you’ll enter the iterative design cycle. Improve the beam based on your findings from the FEA simulation, then simulate again. You should be able to dramatically reduce the maximum stress and bending of the beam over the course of several simulations and redesigns. 

### Part Link 

[ENGR4 Beam Starter Document - Graham and Jacob](https://cvilleschools.onshape.com/documents/92a40a9416b5315e6a429686/w/2b2c3d00de9869597b85e9c4/e/0af744a4e82b10b8a53d9b22)

### Part Image

<img src="images\FDA part 4 image.png" width="500">


### Reflection

Three things went wrong:
* When creating the force, the window that pops up prompt you for a direction based on a mate connecter, an instance and the option to load a region. LOAD THE REGION, without any regions loaded, my design holds 25 lbs of force, but with the loading it holds 5.

<img src="images\FDA part 4.2 image.png" width="500">

     
* Holes in designs are very useful, sense the restrictions were revolved around us not being allowed to create overhangs over 45*, I was at a loss as to how to make the design better, but, we're allowed to use holes at the maximum size of 5mm. These holes take away unnessisary material and allow you to use it elsewhere.
* Corners of builds are considered breakpoints, this is because all of the stress is compiled into one small edge. Use the fillet tool to reduce this problem, but not the chamfer because that tool doesnt allow for curveness, and that's a nesesity for structural integrity.

Improvments:
* N/A, our sedign in more complicated and gholds the same weight due to an unfortunate mishap.
* Designing speed, I spent 8 hours designing this incorrectly, I learned how to OnShape faster and thats it.

# landing Area Part 1 (Functions)

### Assignment Description
In this assignment we used a function to return the area of a triangle from user inputed x,y cordinate points.
## Evidence

### Code
```python
# type: ignore
import time #import time
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0      #Declare point values

def Triangle(Inputv):
    try:
        listvalues = Inputv.split(",")  #split Inputed vaue
        x1 = float(listvalues[0])   #assign each input value its position according to the order of the number in the list
        x2 = float(listvalues[2])
        x3 = float(listvalues[4])
        y1 = float(listvalues[1])
        y2 = float(listvalues[3])
        y3 = float(listvalues[5])
        area = abs(x1*(y2-y3) + x2*(y3 - y1) + x3*(y1 - y2))*.5 #calculate triangle area
        return area
    except ValueError:  #bad triangle
        area = -1
        return area
while True:
    Inputv = input('Enter triangle points in x1,y2,x2,y2,x3,y3') #asks for user input
    PrintValue = Triangle(Inputv)
    if PrintValue > 0:  #state machine asking wether the value is 1:a triangle,2: A wrong user input or 3: correct triangle
        print(PrintValue)
    elif PrintValue == 0:
        print('not valid triangle')   
    elif PrintValue < 0:
        print('Worng user input')    
```

### Video
<img src="images\Landing Area Part 1 gif.gif" width="500">

### Reflection
For this assignment I learned how to use functions together with the input, split and float python functions to input and display values. The most difficult part was wraping my head around how a function worked and how I could use that function to take the inputed values and export an area. I also had issues with properly returning the right values out of my function.
# landing Area Part 2 (Plotting)

### Assignment Description
In this assignment we had to add on to the previous code and now display the triangle or landing area on an OLED display while also calculating area

## Evidence

### Code
```python
 # type: ignore
import busio
import board                                   
import time
import digitalio
from adafruit_display_text import label #import from folder
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle   
displayio.release_displays()

sda_pin = board.GP14    #sets SDA and SCL
scl_pin = board.GP15

splash = displayio.Group()

i2c = busio.I2C(scl_pin, sda_pin)           #Setup for OLED
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP5)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0  
area = 0    #Declare point values
hlinex = Line(0,32,128,32, color=0xFFFF00)
hliney = Line(64,0,64,64, color=0xFFFF00)
circle = Circle(64,32,2, outline=0xFFFF00)

splash.append(circle)   #tell OLED to display lines and origin
splash.append(hlinex)
splash.append(hliney)
display.show(splash)

display.show(splash)

def Trianglef(Inputv):
    try:
        listvalues = Inputv.split(",")  #split Inputed vaue
        x1 = float(listvalues[0])   #assign each input value its position according to the order of the number in the list
        x2 = float(listvalues[2])
        x3 = float(listvalues[4])
        y1 = float(listvalues[1])
        y2 = float(listvalues[3])
        y3 = float(listvalues[5])
        area = abs(x1*(y2-y3) + x2*(y3 - y1) + x3*(y1 - y2))*.5 #calculate triangle area
        return [area,x1,x2,x3,y1,y2,y3]
    except ValueError:  #bad triangle
        x1 = 0  #Stops error with no output
        x2 = 0
        x3 = 0  
        y1 = 0
        y2 = 0  
        y3 = 0
        area = -1
        return [area,x1,x2,x3,y1,y2,y3]
        
while True:
    Inputv = input('Enter triangle points in x1,y2,x2,y2,x3,y3') #asks for user input
    area,x1,x2,x3,y1,y2,y3 = Trianglef(Inputv)
    PrintValue = area
    if PrintValue > 0:  #state machine asking wether the value is 1:a triangle,2: A wrong user input or 3: correct triangle
        print(PrintValue)
        triangle = Triangle(int(x1+64),int(32-y1),int(x2+64),int(32-y2),int(x3+64),int(32-y3),outline=0xFFFF00)
        splash.append(triangle) 
        text_area = label.Label(terminalio.FONT, text=str(area), color=0xFFFF00, x=5, y=5)  #positional information for the text displayed onto the OLED
        splash.append(text_area)
        display.show(splash)
    elif PrintValue == 0: #state machine asking wether the value is 1:a triangle,2: A wrong user input or 3: correct triangle
        print(PrintValue)
        print('not valid triangle')   
    elif PrintValue < 0:
        print('Worng user input')  

```
### Video
<img src="images\Landing Area Part 2 gif.gif" width="500">

### Wiring
<img src="images\Landing PT2.png" width="500">

### Reflection
In this assignment, I had issues with using the display and understanding how to use Splash. append and display show. This included using the triangle and line functions. It was really easy to get the graph setup. Still, by far the hardest part of the assignment was moving the variables from the function collecting the points, and calculating the area inside the triangle function. 



# Morse Code Part 1 (Translation)

### Assignment Description
In this assignment, I had to take a written input and turn it into dots and dashes that I would then print out.

## Evidence

### Code
```python
# type: ignore
import busio
import board                                   
import time

inputv = 0


MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

while True:
    inputv = input("enter text:")
    Uppervalue = inputv.upper()
    for letter in Uppervalue:
        print(MORSE_CODE[letter], end = " ")
```

### Video
<img src="images\Morse Code pt 1.gif" width="500">



### Reflection
In This assignment introduced dictionaries and how to use dictionaries to translate words into dots and dashes. The most difficult part of this assignment was definitely getting the words into the right format and making sure that they where being translated correctly I had to take the dots and dashes and translate them into a on and off sequence for a LED that would "transmit" morse code.



# Morse Code Part 2 (Transmission)

### Assignment Description
In this assignment, I had to take the dots and dashes and translate them into an on and off-sequence for a LED that would "transmit" morse code.

## Evidence

### Code
```python
# type: ignore
import busio
import board                                   
import time
import digitalio

led = digitalio.DigitalInOut(board.GP5) #Sets LED pin
led.direction = digitalio.Direction.OUTPUT

inputv = 0
modifier = 0.05
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier



MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
message = ""
BEEP = {'.': dot_time , '-': dash_time}
while True:
    inputv = input("enter text:")
    Uppervalue = inputv.upper()
    for letter in Uppervalue:
        print(MORSE_CODE[letter], end = " ")
        message = message + " " + MORSE_CODE[letter]
        for character in MORSE_CODE[letter]:
            led.value = True
            time.sleep(BEEP[character])
            led.value = False
            time.sleep(dot_time)
        time.sleep(dash_time)


```

### Video
<img src="images\MorsecodePT2.gif" width="500">

### Wiring
<img src="images\Morse Code Wire .png" width="500">

### Reflection



# Data Part 1 (Storage)

### Assignment Description

## Evidence

### Code
```python

```

### Video
<img src="" width="500">

### Wiring
<img src="" width="500">

### Reflection



# Data Part 2 (Analysis)

### Assignment Description

## Evidence

### Code
```python

```

### Video
<img src="" width="500">

### Wiring
<img src="" width="500">

### Reflection