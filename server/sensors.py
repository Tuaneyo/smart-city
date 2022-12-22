from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
import db
from gpiozero.pins.pigpio import PiGPIOFactory
from operator import le
from threading import Thread
import json
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import time
from datetime import datetime
import math
import db

# BARRIER CONFFIG
factory = PiGPIOFactory()
 
myGPIO=17
 
myCorrection=0
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO, min_pulse_width=minPW,max_pulse_width=maxPW, pin_factory=factory)

timer = 0.03
startCycle = 0
endCycle = 18

waiter=3.2

# PK SENSOR CONFFIG
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


lcd = LCD()
TRIG = 18
ECHO = 6 # space 8
LED_RED = 17
LED_GREEN = 22
LED_RED1 = 26
LED_GREEN1 = 19

lcd = LCD()
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_GREEN,GPIO.OUT)
GPIO.setup(LED_RED,GPIO.OUT)
GPIO.setup(LED_GREEN1,GPIO.OUT)
GPIO.setup(LED_RED1,GPIO.OUT)

GPIO.setwarnings(False)
prev_PK_space = False

# BUTTON FUNC
BUTTON_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
previous_button_state = True

def open_barrier():
  print('Open barrier')
  for value in range(startCycle, endCycle):
    r_value=(float(value)-10)/10
    servo.value=r_value
    sleep(timer)
  sleep(waiter)
  close_barrier()


def close_barrier():
  print('barrier gaat dicht')
  for value in range(endCycle - 1,-1,-1):
    r_value=(float(value)-10)/10
    servo.value=r_value
    sleep(timer)

try:
    while True:
        sleep(0.01)
        button_state = GPIO.input(BUTTON_PIN)
        if button_state != previous_button_state:
          previous_button_state = button_state
          if button_state == GPIO.HIGH:
            r_c = db.register_car()
            if r_c:
              open_barrier()


except KeyboardInterrupt:
    GPIO.cleanup()
    GPIO.cleanup
    GPIO.output(LED_GREEN,GPIO.LOW)
    GPIO.output(LED_RED, GPIO.LOW)  
    GPIO.output(LED_GREEN1,GPIO.LOW)
    GPIO.output(LED_RED1, GPIO.LOW)  
    lcd.clear()   

