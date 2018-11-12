import RPi.GPIO as GPIO
from time import sleep
from robot_module import *
from threading import Thread
from random import choice

blue_led = 27
red_led = 25
yellow_led = 24
green_led = 23

button_1 = 18
button_2 = 19
button_3 = 20
button_4 = 21

buttons = [button_1, button_2, button_3, button_4]
pattern = [choice(buttons), choice(buttons), choice(buttons), choice(buttons)]
inputted_pattern = []

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

'''GPIO.setup(button_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button_4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)'''

        
def ledChecks():
    time = 0
    while True:
        try:
            if abs(int(Game.currentLoc.number) - int(Game.robot_currentLoc.number)) >= 20:
                GPIO.output(green_led, 1)
                sleep(0.4)
                GPIO.output(green_led, 0)
                sleep(0.4)

            elif abs(int(Game.currentLoc.number) - int(Game.robot_currentLoc.number)) >= 10:
                GPIO.output(yellow_led, 1)
                sleep(0.2)
                GPIO.output(yellow_led, 0)
                sleep(0.2)

            elif int(Game.currentLoc.number) == int(Game.robot_currentLoc.number):
                GPIO.output(red_led, 1)
                sleep(0.1)
                GPIO.output(red_led, 0)
                sleep(0.1)
                time += 1
                if time == 50:
                    exit(0)
                    
        except AttributeError:
            continue
                

def debugCheck():    
    if debug:
        GPIO.output(blue_led, 0)
        sleep(0.1)
    if not debug:
        GPIO.output(blue_led, 1)
        sleep(0.1)


leds = Thread(name='leds', target=ledChecks)
leds.start()

'''def buttonOneCheck():
    global inputted_pattern
    while GPIO.input(button_1) == 1:
        inputted_pattern.append(button_1)
        print inputted_pattern
        break
        
        
def buttonTwoCheck():
    global inputted_pattern
    while GPIO.input(button_2) == 1:
        inputted_pattern.append(button_2)
        print inputted_pattern
        break

def buttonThreeCheck():
    global inputted_pattern
    while GPIO.input(button_3) == 1:
        inputted_pattern.append(button_3)
        print inputted_pattern
        break

def buttonFourCheck():
    global inputted_pattern
    while GPIO.input(button_4) == 1:
        inputted_pattern.append(button_4)
        print inputted_pattern
        break

def buttonsCheck():
    global inputted_pattern
    while inputted_pattern < 4:
        if (GPIO.input(button_1) == 1):
            inputted_pattern.append(button_1)
            print inputted_pattern
            break
                
        if (GPIO.input(button_2) == 1):
            inputted_pattern.append(button_2)
            print inputted_pattern
            break
                
        if (GPIO.input(button_3) == 1):
            inputted_pattern.append(button_3)
            print inputted_pattern
            break
                
        if (GPIO.input(button_4) == 1):
            inputted_pattern.append(button_4)
            print inputted_pattern
            break

    buttonsCheck()

    elif inputted_pattern == pattern:
        exit(0)
    else:
        inputted_pattern = []

    bc = Thread(name='buttons', target=buttonsCheck)
    b1 = Thread(name='button 1', target=buttonOneCheck)
    b2 = Thread(name='button 2', target=buttonTwoCheck)
    b3 = Thread(name='button 3', target=buttonThreeCheck)
    b4 = Thread(name='button 4', target=buttonFourCheck)

    bc.start()
    b1.start()
    b2.start()
    b3.start()
    b4.start()'''

