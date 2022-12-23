from threading import Thread
import barrier
import PK_sensor 

barrierThread = Thread(target = barrier.run_barrier()).start() 
pkThread = Thread(target = PK_sensor.run_PK()).start() 