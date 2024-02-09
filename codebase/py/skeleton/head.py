#!/usr/bin/python3

import RPi.GPIO as GPIO
import gpiozero
import time
import piplates.DAQCplate as DAQC

GPIO.setmode(GPIO.BCM)
#GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


for m in range(10):
    GPIO.output(21,False)
    time.sleep(0.2)
    GPIO.output(21,True)
    time.sleep(0.2)

GPIO.output(21,False)

from gpiozero import Buzzer 


bz = Buzzer(20) 
while True: 
    bz.off() 
    time.sleep(0.1)
    r = DAQC.getRANGE(0,0,'c')
    if r < 20:
        bz.on() 
        time.sleep(0.1)
        

