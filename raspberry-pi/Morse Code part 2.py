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

