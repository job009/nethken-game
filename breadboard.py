import RPi.GPIO as GPIO
from time import sleep
from robot_module import *
from threading import Thread

blue_led = 27
red_led = 25
yellow_led = 24
green_led = 23

button_1 = 18
button_2 = 19
button_3 = 20
button_4 = 21

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.setup(button_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def green_check():
    while Game.currentLoc == Game.robot_currentLoc:
        GPIO.output(green_led, 0)
        sleep(0.9)
        GPIO.output(green_led, 1)
        sleep(0.9)

def yellow_check():
    while Game.currentLoc == Game.robot_currentLoc:
        GPIO.output(yellow_led, 0)
        sleep(0.4)
        GPIO.output(yellow_led, 1)
        sleep(0.4)

def red_check():
    while Game.currentLoc == Game.robot_currentLoc:
        GPIO.output(red_led, 0)
        sleep(0.1)
        GPIO.output(red_led, 1)
        sleep(0.1)

def debug_check():    
    while debug:
        GPIO.output(blue_led, 0)
        sleep(0.1)
        GPIO.output(blue_led, 1)
        sleep(0)
    while not debug:
        GPIO.output(blue_led, 1)
        sleep(0.1)
        GPIO.output(blue_led, 0)
        sleep(0)

def led_checks():
    g = Thread(name='green', target=green_check)
    y = Thread(name='yellow', target=yellow_check)
    r = Thread(name='red', target=red_check)
    d = Thread(name='debug', target=debug_check)

    g.start()
    y.start()
    r.start()
    d.start()
