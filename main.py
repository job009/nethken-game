#################################################################
# Name: JonMichael Book, Logan Simmons, Elise Deimel
# Date: 2018-10-##
# Description: (Name of Project Here)
#################################################################

from Tkinter import *
from game_module import Game

window = Tk()
window.title("Robot Ravage")
window.iconbitmap('icon.ico')

g = Game(window)
g.play()

window.mainloop()