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