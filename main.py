#################################################################
# Name: JonMichael Book, Logan Simmons, Elise Deimel
# Date: 2018-10-##
# Description: Robot Ravage
#################################################################

from Tkinter import *
import RPi.GPIO as GPIO
from game_module import Game
from robot_module import run
from breadboard import ledChecks
from config import *
from threading import Thread 

def background_1():
    run()

def background_2():
    ledChecks()

def foreground():
    window = Tk()
    window.title("Robot Ravage")
    g = Game(window)
    g.play()
    window.mainloop()


b1 = Thread(name='background_1', target=background_1)
b2 = Thread(name='background_2', target=background_2)
f = Thread(name='foreground', target=foreground)

b1.start()
b2.start()
f.start()
