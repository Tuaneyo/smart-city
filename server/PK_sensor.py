from operator import le
from threading import Thread
import json
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import time
from datetime import datetime
import math
import db

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


lcd = LCD()
TRIG = 18
ECHO = 6 # space 8
PARKING_SPACE = 6
LED_RED = 17
LED_GREEN = 22
LED_RED1 = 26
LED_GREEN1 = 19

# def PK_1():
#     global TRIG
#     TRIG = 21
#     ECHO = 20
#     LED_RED = 26
#     LED_GREEN = 19

# def PK_2():
#     TRIG = 23   
#     ECHO = 24
#     LED_RED = 17
#     # LED_YELLOW = 27
#     LED_GREEN = 22

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

try:
    lcd.clear()
    lcd.text("Waiting for ",1)
    lcd.text("sensor to Settle",2)
    while True:
        GPIO.output(TRIG, False)
        
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 1)
        
        if distance >= 8:
            GPIO.output(LED_GREEN, GPIO.HIGH)
            GPIO.output(LED_GREEN1, GPIO.HIGH)
            # GPIO.output(LED_RED1, GPIO.HIGH)
            
            GPIO.output(LED_RED, GPIO.LOW) 
            PK_space = False # Space free
            db.save_pk_spaces(PARKING_SPACE, PK_space)
            print('groen')
            if prev_PK_space != PK_space:
                prev_PK_space = False
                end_time = datetime.now()
                db.save_car_parked(begin_time, end_time)
                print('send db timestamp end')
        else:
            GPIO.output(LED_GREEN, GPIO.LOW)
            PK_space = True # Space occupied
            GPIO.output(LED_RED, GPIO.HIGH)
            db.save_pk_spaces(PARKING_SPACE, PK_space)
            print('rood')
            if prev_PK_space != PK_space:
                prev_PK_space = True
                begin_time = datetime.now()
                print('begin_time ', begin_time)
                print('send db timestamp begin')
    
        time.sleep(2)
        lcd.clear()
        spaces_text = db.get_free_space()
        if spaces_text:
            lcd.text("Plek {} vrij".format(spaces_text), 1)
        else:
            lcd.text("Garage is vol", 1)
    
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup
    GPIO.output(LED_GREEN,GPIO.LOW)
    GPIO.output(LED_RED, GPIO.LOW)  
    GPIO.output(LED_GREEN1,GPIO.LOW)
    GPIO.output(LED_RED1, GPIO.LOW)  
    lcd.clear()                                                                                                                                                                                                                                            
                             
