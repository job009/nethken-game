from random import choice, randint
from time import sleep
from game_module import Game
from modules import *
from config import *
from breadboard import *


def run():
    while robot_active:
        if type(Game.robot_currentLoc) is Hallway:
            rooms = Game.robot_currentLoc.rooms
            hallways = Game.robot_currentLoc.hallways

            if randint(0, 100) < 60:
                robot_loc_type = rooms
            else:
                robot_loc_type = hallways

            if robot_loc_type == rooms:
                robot_location = choice(rooms.keys())
                Game.robot_currentLoc = rooms[robot_location]
                if debug:
                    print "-> " + robot_location

            elif robot_loc_type == hallways:
                robot_location = choice(hallways.keys())
                Game.robot_currentLoc = hallways[robot_location]
                if debug:
                    print "-> " + robot_location

        elif type(Game.robot_currentLoc) is Room:
            exits = Game.robot_currentLoc.exits

            robot_location = choice(exits.keys())
            Game.robot_currentLoc = exits[robot_location]
            if debug:
                print "-> " + robot_location

        if difficulty.lower() == "easy":
            delay = randint(20, 30)
            
        elif difficulty.lower() == "normal":
            delay = randint(10, 20)
            
        elif difficulty.lower() == "hard":
            delay = randint(5, 10)

            
        if debug:
            print "\nDelay: {}".format(delay)

        sleep(delay)
