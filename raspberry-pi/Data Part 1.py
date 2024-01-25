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
tilt = False


while True:
    with open("/data.csv", "a") as datalog:
        if mpu.acceleration[2] < 9:
            led.value = False
            tilt = False
        else:
            led.value = True
            tilt = True 
        Timeprint = time.monotonic()
        datalog.write(f"{float(Timeprint)},{mpu.gyro[0],3},{mpu.gyro[1],3},{mpu.gyro[2],3},{mpu.acceleration[2]},{tilt}\n")
        datalog.flush()
        time.sleep(0.25)