#!/usr/bin/python3

import RPi.GPIO as GPIO
import gpiozero
import time
import piplates.DAQCplate as DAQC
import pygame
import os
from gpiozero import Buzzer
import random

# Introduce background thingielingie

class skeletor():

    def gpio_setup(self):
        self.GPIO_EYES = 21
        self.GPIO_BUZZ = 20

        GPIO.setmode(GPIO.BCM)
        #GPIO.setup(20, GPIO.OUT)
        GPIO.setup(self.GPIO_EYES, GPIO.OUT)

    def init_sounds(self):
        pygame.mixer.init()
        self.sounds = []

        sound_path = "/home/pi/"
        sound_files = ["287.wav",
                       "cackle3.wav",
                       "hauntedhouse.wav",
                       "lach01.wav",
                       "police_s.wav",
                       "Swamp_Background_web.wav",
                       "witches_house.wav",
                       "wlaugh.wav"]
        for sound_file in sound_files:
            my_sound = pygame.mixer.Sound(os.path.join(sound_path, sound_file))        
            self.sounds.append(my_sound)
        
    def __init__(self):
        self.gpio_setup()
        self.init_sounds()
        self.buzzer = Buzzer(self.GPIO_BUZZ)

    def blink(self, blinks=10):
        # Blinks the eyes
        for m in range(blinks):
            GPIO.output(self.GPIO_EYES,False)
            time.sleep(0.2)
            GPIO.output(self.GPIO_EYES,True)
            time.sleep(0.2)
        GPIO.output(self.GPIO_EYES,False)

    def buzz(self):
        self.buzzer.on()

    def huzz(self):
        self.buzzer.off()

    def prox(self):
        # Handle errors here
        try:
            # pins are digital 0 and analog 0 ( I think )
            r = DAQC.getRANGE(0,0,'c')
        except:
            r = 1e9
        return r

    def howl(self, pick_one = True):

        if pick_one:            
            the_sound = random.choice(self.sounds)

        the_sound.play()
        pygame.time.wait(int(the_sound.get_length()*1000))

def main():

    guy = skeletor()
    guy.blink()

    guy.buzz()
    time.sleep(1)

    guy.buzz()
    time.sleep(1)


    
    while True:
        guy.huzz()
        if guy.prox() < 5:
            DAQC.setDOUTbit(0,5)
            guy.howl()
            time.sleep(0.1)
            DAQC.clrDOUTbit(0,5)            

if __name__ == "__main__":
    main()
