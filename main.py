#################################################################
# Name: JonMichael Book, Logan Simmons, Elise Deimel
# Date: 2018-10-##
# Description: (Name of Project Here)
#################################################################

from Tkinter import *
from game_module import Game
from robot_module import run
from config import *
import threading


def background():
    run()

def foreground():
    window = Tk()
    window.title("Robot Ravage")
    window.iconbitmap('icon.ico')
    g = Game(window)
    g.play()

    window.mainloop()

b = threading.Thread(name='background', target=background)
f = threading.Thread(name='foreground', target=foreground)

b.start()
f.start()
