'''
bisa menggunakan python3 and install package RPi dengan perintah pip3
script ini akan menyalakan lampu relay sejenak setelah itu mematikannya
referensi: https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/
http://wiki.sunfounder.cc/index.php?title=2_Channel_5V_Relay_Module
'''

import RPi.GPIO as GPIO
from time import sleep
import socket

GPIO.setmode(GPIO.BOARD)
PIN_1 = 16
PIN_2 = 13
name = socket.gethostname()

def openGate():
    GPIO.setup(PIN_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PIN_2, GPIO.OUT, initial=GPIO.LOW)
    sleep(0.5)
    GPIO.setup(PIN_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_2, GPIO.OUT, initial=GPIO.HIGH)
   
