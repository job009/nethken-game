from random import choice, randint
from time import sleep, time

rooms = [x for x in range(6)]

robot_status = True
robot_location = None
player_location = None

num = choice(rooms)
while robot_status:
    move = choice([num + 1, num - 1])
    if move in rooms:
        pass
    else:
        move = num
    print move
    num = move
    sleep(0.5)