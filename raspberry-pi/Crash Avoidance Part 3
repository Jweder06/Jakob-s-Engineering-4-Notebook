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