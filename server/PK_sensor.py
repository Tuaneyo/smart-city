from operator import le
from threading import Thread
import json
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import time
from datetime import datetime
import math
import db

def run_PK():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    lcd = LCD()
    TRIG = 18
    ECHO = 6 # space 8
    PARKING_SPACE = 1
    LED_RED = 19
    LED_GREEN = 26

    GPIO.setwarnings(False)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(LED_GREEN,GPIO.OUT)
    GPIO.setup(LED_RED,GPIO.OUT)

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
                
                GPIO.output(LED_RED, GPIO.LOW) 
                PK_space = False # Space free
                db.save_pk_spaces(PARKING_SPACE, PK_space)
                if prev_PK_space != PK_space:
                    prev_PK_space = False
                    end_time = datetime.now()
                    db.save_car_parked(begin_time, end_time, PARKING_SPACE)
            else:
                GPIO.output(LED_GREEN, GPIO.LOW)
                PK_space = True # Space occupied
                GPIO.output(LED_RED, GPIO.HIGH)
                db.save_pk_spaces(PARKING_SPACE, PK_space)
                print('rood')
                if prev_PK_space != PK_space:
                    prev_PK_space = True
                    begin_time = datetime.now()
        
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
        lcd.clear()                                                                                                                                                                                                                                            