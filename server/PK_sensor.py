from operator import le
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import time
from datetime import datetime
import math
# import db

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


lcd = LCD()
TRIG = 18
ECHO = 6 # space 8
LED_RED = 17
# LED_YELLOW = 27
LED_GREEN = 22

lcd.text("Distance measurement",1)
lcd.text("in Progress",2)
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
            # db.save_pk_spaces(ECHO, PK_space)
            print('groen')
            if prev_PK_space != PK_space:
                prev_PK_space = False
                end_time = datetime.now()
                print("end_time ", end_time)
                delta = end_time - begin_time
                print("Delta: ", math.floor(delta.total_seconds()))
                print('send db timestamp park space occupied end')
        else:
            GPIO.output(LED_GREEN, GPIO.LOW)
            PK_space = True # Space occupied
            GPIO.output(LED_RED, GPIO.HIGH)
            # db.save_pk_spaces(ECHO, PK_space)
            print('rood')
            if prev_PK_space != PK_space:
                prev_PK_space = True
                begin_time = datetime.now()
                print('begin_time ', begin_time)
                print('send db timestamp park space occupied begin')
    
        time.sleep(2)
        lcd.clear()
        # lcd.text("Plek {} vrij".format(db.get_free_space()), 1) 
    
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup
    GPIO.output(LED_GREEN,GPIO.LOW)
    GPIO.output(LED_RED, GPIO.LOW)  
    lcd.clear() 

    

                                                                                                                                                                                                                                                              
