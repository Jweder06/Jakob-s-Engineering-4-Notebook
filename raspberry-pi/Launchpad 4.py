# type: ignore
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT
Rled = digitalio.DigitalInOut(board.GP2)
Rled.direction = digitalio.Direction.OUTPUT 
Button = digitalio.DigitalInOut(board.GP1)
Button.pull = digitalio.Pull.DOWN
pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
Count_time = 11
Button_state = 0
Start_value = 0
while True:
     if Button.value == True and Button_state == 0:
         Button_state = 1
         Start_value = Start_value + 1
     if Button.value == False:
         Button_state = 0
     if Count_time >= 1 and Start_value == 1:
          Gled.value = False
          Count_time = Count_time - 1
          Rled.value = True
          time.sleep(.5)
          Rled.value = False
          time.sleep(.5)
          print(Count_time)
          servo1.angle = 180
     if Count_time == 0 and Start_value == 1:
          print("Launch")
          Gled.value = True
          Rled.value = False
          time.sleep(2)
          servo1.angle = 0
     if   Start_value == 2:
         print("abort")
     if Start_value == 3:
         Start_value = 1
         Count_time = 11