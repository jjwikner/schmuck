#!/usr/bin/python3

import RPi.GPIO as GPIO
import gpiozero
import time, sys, os, random
from picamera import PiCamera
import piplates.DAQCplate as DAQC
import pygame
from gpiozero import Buzzer
from ascii_magic import AsciiArt
import threading
import subprocess
import keyboard
import mysql.connector
from datetime import datetime

# This sucks --> from pynput.keyboard import Key, Listener

# ----------------------------------
# Introduce background thingielingie
# ----------------------------------

class skeletor():

    #def handle_key(self, key):
    #    if key == Key.tab:
    #        self.blink()
            
    def gpio_setup(self):
        self.GPIO_EYES = 20
        self.GPIO_BUZZ = 21
        self.GPIO_BUTTON = 26

        GPIO.setmode(GPIO.BCM)
        # GPIO.setup(20, GPIO.OUT)
        # GPIO.setup(self.GPIO_EYES, GPIO.OUT)
        # GPIO.setup(self.GPIO_BUTTON, GPIO.IN)
        
    def init_sounds(self):
        pygame.mixer.init()
        self.sounds = []

        sound_path = "../../../database/sound/"
       
        sound_files = ["287.wav",
                       "cackle3.wav",
                       "hauntedhouse.wav",
                       "lach01.wav",
                       "police_s.wav",
                       "Swamp_Background_web.wav",
                       "witches_house.wav",
                       "untitled.wav",
                       "wlaugh.wav"]
        for sound_file in sound_files:
            my_sound = pygame.mixer.Sound(os.path.join(sound_path, sound_file))        
            self.sounds.append(my_sound)

    def init_camera(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        self.fig_path = "/var/www/html/figs"
        
        # time.sleep(2)

    def snap_photo(self, display=True):
        filename = f"{time.time()}".replace('.','_')+".jpg"
        self.camera.capture(os.path.join(self.fig_path, filename))
        # Add filename to database.
        # Create database
    
        if display:
            my_art = AsciiArt.from_image(os.path.join(self.fig_path, filename))
            my_art.to_terminal()
        
            
    def __init__(self):
        self.gpio_setup()
        self.detect = True
        self.init_sounds()
        self.init_camera()
        self.buzzer = Buzzer(self.GPIO_BUZZ)
        self.PIPLATE_BOARD_NO = 0
        self.DAQC_EYES_PIN = 4
        self.DAQC_ARM_PIN = 5 # Digital pin!
        self.range_channel = 0
        self.DAQC_USE_EYES = True
        self.arm_lap_time = 2.0 # seconds
        self.gesture_last_time = 0
        self.gesture_distance = 52

        self.db =  mysql.connector.connect(user='root', 
                                           password='pass1234',
                                           host='127.0.0.1',
                                           database='skeletor')
        self.db_ptr = self.db.cursor()
    
    def setup_button(self):
        GPIO.setup(self.GPIO_BUTTON, GPIO.IN, GPIO.PUD_UP)
        self.button = gpiozero.Button(self.GPIO_BUTTON, pull_up=True,
                                      active_state=None, bounce_time=0.01,
                                      hold_time=0.2, hold_repeat=False, pin_factory=None)
        self.button.when_pressed = self.press_button
        self.button.when_released = self.release_button
        
    def press_button(self):
        print("Button is pressed!")
        self.blink_eyes()
        # Start radio
                
    def release_button(self):
        print("Button is released!")
        self.close_eyes()
        
    def close_eyes(self):
        if self.DAQC_USE_EYES:
            DAQC.setDOUTbit(self.PIPLATE_BOARD_NO, self.DAQC_EYES_PIN)
        else:
            GPIO.output(self.GPIO_EYES,False)
            
    def open_eyes(self):
        if self.DAQC_USE_EYES:
            DAQC.clrDOUTbit(self.PIPLATE_BOARD_NO, self.DAQC_EYES_PIN)
        else:
            GPIO.output(self.GPIO_EYES,True)

    def blink(self, blink_eyess=3):
        self.blink_eyes(blink_eyess=blink_eyess)
        
    def blink_eyes(self, blink_eyess=10):
        # Blink_Eyess the eyes
        # Set the output bits differently
        self.eyes_blink_eyes_time = 0.1
        
        for m in range(blink_eyess):
            self.open_eyes()
            time.sleep(self.eyes_blink_eyes_time)
            self.close_eyes()
            time.sleep(self.eyes_blink_eyes_time)

    def buzz(self):
        self.buzzer.on()

    def huzz(self):
        self.buzzer.off()

    def crunch(self, clicks = 10):
        for m in range(clicks):
            self.buzz()
            time.sleep(0.2)
            self.huzz()
        
    def prox(self):
        # Handle errors here
        try:
            # pins are digital 0 and analog 0 ( I think )
            r = DAQC.getRANGE(self.PIPLATE_BOARD_NO, self.range_channel, 'c')
        except:
            r = 1e9
        return r

    def howl(self, pick_one = True):

        if pick_one:            
            the_sound = random.choice(self.sounds)

        the_sound.play()
        pygame.time.wait(int(the_sound.get_length()*1000))

    def move_arm(self):
        # Move one rotation        
        now = time.time()
        self.start_moving()
        while time.time() < now + self.arm_lap_time:
            time.sleep(0.02)
        self.stop_moving()

    def start_moving(self):
        DAQC.setDOUTbit(self.PIPLATE_BOARD_NO, self.DAQC_ARM_PIN)
        
    def stop_moving(self):
        DAQC.clrDOUTbit(self.PIPLATE_BOARD_NO, self.DAQC_ARM_PIN)
        
    def startup(self):
        self.setup_button()
        th1= threading.Thread(target=self.blink_eyes)
        th2= threading.Thread(target=self.crunch)
        th1.start()
        th2.start()
        th1.join()
        th2.join()
        
        #self.snap_photo()
        #self.howl()
        #self.huzz()        
        #self.move_arm()

    def close(self):
        print("Burying the skeleton.")
        # Turn off all the DAQC pins.
        self.close_eyes()
        return

    def gesture_action(self):
        self.start_moving()
        # Threads can be initiated in __init__
        # Use one thread for each activity.
        # With join, it will wait for all to finish.
        th1 = threading.Thread(target=self.howl)
        th2 = threading.Thread(target=self.blink_eyes)
        #self.howl()
        # time.sleep(0.1)
        th1.start()
        th2.start()
        th1.join()
        th2.join()
        self.stop_moving()
        self.gesture_last_time = time.time()

    def gesture_wait(self):
        time.sleep(0.01)
        
    def gesture_detect(self):
        # Idea -- detect two gestures within certain period of time.
        # Save the time after last tiome
        if self.detect:
            if (self.prox() < self.gesture_distance):
                now = time.time()
                if (now - self.gesture_last_time) < 20:
                    self.blink_eyes(2)
                self.gesture_wait()
                self.gesture_action()
        
    def check_play_file(self, playfile="interact.txt"):
        if os.path.exists(playfile):
            with open(playfile,"r") as f:
                linez = f.readlines()
                for line in linez:
                    if "blink" in line.rstrip():
                        self.blink_eyes()
                    if "howl" in line.rstrip():
                        self.howl()
                    if "move" in line.rstrip():
                        self.move_arm()
                    # more action can be done here    
            os.remove("interact.txt")
          

    def click(self):
        self.crunch()
        
    def check_db(self):

        self.db_ptr = self.db.cursor()
        self.db_ptr.execute("SELECT Move, Howl, Blink, Click, Epoq, Photo, Quit, Start, Detect from Actions")
        for Move, Howl, Blink, Click, Epoq, Photo, Quit, Start, Detect in self.db_ptr:
            seconds_since = (datetime.fromtimestamp(time.time())-Epoq).total_seconds()
            if seconds_since < 3:
                if (Blink > 0):
                    print("Blinking")
                    self.blink_eyes(Blink+10)
                if (Howl > 0):
                    print("Howling")
                    self.howl()
                if (Click > 0):
                    print("Crunching")
                    self.crunch()
                if (Move > 0):
                    print("Chilling")
                    self.move_arm()                
                if (Photo > 0):
                    print("Chilling")
                    self.snap_photo()
                    
                if (Quit > 0):
                    print("Quitting")
                    self.hibernate()

                         
                if (Start > 0):
                    print("Starting")
                    

                if (Detect > 0):
                    self.detect = not self.detect
                    time.sleep(2)

        self.db.commit()

    def hibernate(self):
        exit()
        
# ----------------------------------
"""
TODO:
Add exception pås ctrl+c
"""

def main():

    guy = skeletor()
    guy.startup()
    #with Listener(on_press=guy.handle_key) as listener:
    #    listener.join()
    #    time.sleep(0.1)
    #while True:
    #    if keyboard.read_key() == "b":
    #        guy.blink()
            
    while True:
        time.sleep(1)
        guy.gesture_detect()
        guy.check_db()
        guy.blink(4)
        
    guy.close()

            
# ----------------------------------

if __name__ == "__main__":
    main()


    """
CREATE TABLE `skeletor`.`Actions` ( `Move` INT NOT NULL DEFAULT '0' , `Howl` INT NOT NULL DEFAULT '0' , `Blink` INT NOT NULL DEFAULT '0' , `Click` INT NOT NULL , `Epoq` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , `Photo` INT NOT NULL , `Quit` INT NOT NULL DEFAULT '0' , `Start` INT NOT NULL DEFAULT '0' , `Detect` INT NOT NULL DEFAULT '0' ) ENGINE = InnoDB; """
