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

i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP5)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0      #Declare point values

title = "Graph"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
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
        x1 = 0
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
    print(area,x1,x2,x3,y1,y2,y3)
    if PrintValue > 0:  #state machine asking wether the value is 1:a triangle,2: A wrong user input or 3: correct triangle
        print(PrintValue)
        triangle = Triangle(int(x1-64),int(32-y3),int(x2-64),int(32-y2),int(x3-64),int(32-y3),outline=0xFFFF00)
        splash.append(triangle)
    elif PrintValue == 0:
        print('not valid triangle')   
    elif PrintValue < 0:
        print('Worng user input')   


