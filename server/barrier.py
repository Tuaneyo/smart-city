from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
import db
from gpiozero.pins.pigpio import PiGPIOFactory

def run_barrier():
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

  # BUTTON FUNC

  BUTTON_PIN = 12
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  previous_button_state = True

  BUTTON_PIN_OUT = 23
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BUTTON_PIN_OUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  previous_button_state_out = True


  try:
      while True:
          sleep(0.01)
          button_state = GPIO.input(BUTTON_PIN)
          if button_state != previous_button_state:
            previous_button_state = button_state
            if button_state == GPIO.HIGH:
              r_c = db.register_car('increment')
              if r_c == False:
                open_barrier()


          button_state = GPIO.input(BUTTON_PIN_OUT)
          if button_state != previous_button_state_out:
            previous_button_state_out = button_state
            if button_state == GPIO.HIGH:
                print('pin 25')
                open_barrier()
                db.register_car('decrement')



  except KeyboardInterrupt:
      GPIO.cleanup()