from Tkinter import *
from random import randint
from char_module import Character
from grab_module import Grabbables
from room_module import Room
from hallway_module import Hallway
import Descriptions
import Events

WIDTH = 720
HEIGHT = 960

class Game(Frame):
        def __init__(self, parent):
                Frame.__init__(self, parent)
                # list to keep track of all the rooms
                self.rooms = []
                # list to keep track of all the grabbables
                self.grabbables = []
                # variable to keep track of encounters
                self.encounter = None
                # variables to keep track of victory/lose conditions
                self.death = False
                self.victory = False
        
        # function to create a character pending GUI implementation
        def createCharacter(self):
                global character
                # test character, finished function will implement the GUI and allow for 
                # customization
                character = Character("Dima Ulrich")


        def createRooms(self):
                # create the rooms and give them meaningful names
                exit_1 = Room("Exit 1", "", "")
                exit_2 = Room("Exit 2", "", "")
                exit_3 = Room("Exit 3", "", "")
                exit_4 = Room("Exit 4", "", "")
                exit_5 = Room("Exit 5", "", "")
                exit_6 = Room("Exit 6", "", "")

                hallway_1 = Hallway("Hallway 1", 1, "")
                hallway_1.addExit("exit_4", exit_4)

                hallway_2 = Hallway("Hallway 2", 2, "")
                hallway_2.addExit("exit_3", exit_3)

                hallway_3 = Hallway("Hallway 3", 3, "")
                hallway_3.addExit("exit_1", exit_1)
                hallway_3.addExit("exit_2", exit_2)

                hallway_4 = Hallway("Hallway 4", 4, "")
                hallway_4.addExit("exit_5", exit_5)

                hallway_5 = Hallway("Hallway 5", 5, "")
                hallway_5.addExit("exit_6", exit_6)

                hallway_1.addHallway("hallway_2", hallway_2)
                hallway_2.addHallway("hallway_1", hallway_1)
                hallway_2.addHallway("hallway_3", hallway_3)
                hallway_3.addHallway("hallway_2", hallway_2)
                hallway_3.addHallway("hallway_4", hallway_4)
                hallway_4.addHallway("hallway_3", hallway_3)
                hallway_4.addHallway("hallway_5", hallway_5)
                hallway_5.addHallway("hallway_4", hallway_4)


                _160 = Room("Locked Classroom", "160", "")
                _160.addExit("hall", hallway_5)

                _158 = Room("Locked Classroom", "158", "")
                _158.addExit("hall", hallway_5)

                _157 = Room("Machine Vision/AI (Robotics Lab)", "157", "roboticslab.gif")
                _157.addExit("hall", hallway_5)

                _156 = Room("Classroom", "156", "")
                _156.addExit("hall", hallway_5)

                _155 = Room("Dr. Ibrahim Abdoulahi's Office", "155", "")
                _155.addExit("hall", hallway_5)

                _154 = Room("Locked Classroom","149","")
                _154.addExit("hall", hallway_5)

                _153 = Room("Classroom","153","")
                _153.addExit("hall", hallway_5)

                _152 = Room("Bathroom","152","")
                _152.addExit("hall", hallway_5)

                _151 = Room("Optoelectronics Lab","151","")
                _151.addExit("hall", hallway_4)

                _149 = Room("Dr. Miguel Gates' Office","149","")
                _149.addExit("hall", hallway_4)

                _148 = Room("Storage", "148" ,"")
                _148.addExit("hall", hallway_4)

                _147 = Room("Dr. Andrey Timofeyev's Office","147","")
                _147.addExit("hall", hallway_4)

                _146 = Room("Locked Classroom", "146" ,"")
                _146.addExit("hall", hallway_4)

                _145 = Room("Classroom","145","")
                _145.addExit("hall", hallway_4)

                _144 = Room("Computer Lab", "144","")
                _144.addExit("hall", hallway_4)

                _143 = Room("Unoccupied Office","143","")
                _143.addExit("hall", hallway_4)

                _142 = Room("The Grid", "142", "")
                _142.addExit("hall", hallway_4)

                _141 = Room("Charlotte Wilkerson's Office","141","")
                _141.addExit("hall", hallway_4)

                _140 = Room("Big Classroom","140","")
                _140.addExit("hall", hallway_3)

                _138 = Room("Storage", "138", "")
                _138.addExit("hall", hallway_3)

                _136 = Room("Conference Room", "136", "")
                _136.addExit("hall", hallway_3)

                _134 = Room("Faculty Bathroom","134","")
                _134.addExit("hall", hallway_3)

                _132 = Room("Janitor" , "132", "")
                _132.addExit("hall", hallway_3)

                _128 = Room("Bathroom", "128", "")
                _128.addExit("hall", hallway_3)
                _128.addItem("toilet_paper", "")
                _128.addGrabbable("toilet_paper")

                _127 = Room("Dean Waiting Room", "127", "")
                _127.addExit("hall", hallway_2)

                _125 = Room("Office", "125", "")
                _125.addExit("hall", hallway_2)

                _123 = Room("Office", "123", "")
                _123.addExit("hall", hallway_2)

                _122 = Room("Classroom", "122", "")
                _122.addExit("hall", hallway_2)

                _121 = Room("Dr. Galen E. Turner's Office","121","")
                _121.addExit("hall", hallway_2)

                _120 = Room("Classroom", "120", "")
                _120.addExit("hall", hallway_2)

                _119 = Room("Dr. Ben Choi's Office","119","")
                _119.addExit("hall", hallway_2)

                _118 = Room("Storage", "118", "")
                _118.addExit("hall", hallway_2)

                _117 = Room("Dr. Ben Drozdenso's Office","117","")
                _117.addExit("hall", hallway_2)

                _115 = Room("Dr. Michael O'Neal's Office","115", "")
                _115.addExit("hall", hallway_2)

                _113 = Room("Office Extension", "113", "")
                _113.addExit("hall", hallway_2)

                _111 = Room("Unoccupied Office","111","")
                _111.addExit("hall", hallway_2)

                _107 = None

                _106 = Room("Instrument Room", "106", "")
                _106.addExit("hall", hallway_1)

                _105 = Room("Classroom", "105", "")
                _105.addExit("hall", hallway_1)

                _104 = Room("Power System Labs","104","")
                _104.addExit("hall", hallway_1)

                _103 = Room("Machinary Classroom","103","")
                _103.addExit("hall", hallway_1)

                _102 = Room("Electrical Distribution","102","")
                _102.addExit("hall", hallway_1)

                _101 = Room("Data Mining Lab","101","")
                _101.addExit("hall", hallway_1)

                _100 = Room("Power Systems Lab", "100", "")
                _100.addExit("hall", hallway_1)


                hallway_1.addRoom("100", _100)
                hallway_1.addRoom("101", _101)
                hallway_1.addRoom("102", _102)
                hallway_1.addRoom("103", _103)
                hallway_1.addRoom("104", _104)
                hallway_1.addRoom("105", _105)
                hallway_1.addRoom("106", _106)
                hallway_1.addRoom("107", _107)

                hallway_2.addRoom("111", _111)
                hallway_2.addRoom("113", _113)
                hallway_2.addRoom("115", _115)
                hallway_2.addRoom("117", _117)
                hallway_2.addRoom("118", _118)
                hallway_2.addRoom("119", _119)
                hallway_2.addRoom("120", _120)
                hallway_2.addRoom("121", _121)
                hallway_2.addRoom("122", _122)
                hallway_2.addRoom("123", _123)

                hallway_3.addRoom("127", _127)
                hallway_3.addRoom("128", _128)
                hallway_3.addRoom("132", _132)
                hallway_3.addRoom("134", _134)
                hallway_3.addRoom("136", _136)
                hallway_3.addRoom("138", _138)
                hallway_3.addRoom("140", _140)
                hallway_3.addRoom("170", None)

                Game.currentRoom = _128
                Game.inventory = []

        def setupGUI(self):
                self.pack(fill=BOTH, expand=1)
                Game.player_input = Entry(self, bg="white")
                Game.player_input.bind("<Return>", self.process)
#                Game.player_input.bind("m", self.map)
                Game.player_input.pack(side=BOTTOM, fill=X)
                Game.player_input.focus()

                img = None
                Game.image = Label(self, width=WIDTH / 2, image=img)
                Game.image.image = img
                Game.image.pack(side=LEFT, fill=Y)
                Game.image.pack_propagate(False)

                text_frame = Frame(self, width=WIDTH / 2)
                Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
                Game.text.pack(fill=Y, expand=1)
                text_frame.pack(side=RIGHT, fill=Y)
                text_frame.pack_propagate(False)

        def setRoomImage(self):
                Game.img = PhotoImage(file=Game.currentRoom.image)

                Game.image.config(image=Game.img)
                Game.image.image = Game.img

        def setStatus(self, status):
                global character
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0", END)
                Game.text.insert(END, str(Game.currentRoom) +\
                                 "\n\nYou are carrying: " + str(Game.inventory) +\
                                 "\n\n" + status)
                Game.text.config(state=DISABLED)
        
                      
                      
        def play(self):
                self.createCharacter()
                self.createRooms()
                self.setupGUI()
                self.setRoomImage()
                # set status with intro
                self.setStatus(Events.intro)


        def process(self, event):
                # check to see if the player has won or lost first
                if (self.victory == True or self.death == True):
                        exit(0)
                action = Game.player_input.get()
                action = action.lower()
                response = "I don't understand. Try verb/noun. Valid verbs are go, look, and take. You can also use 'character' to view your status."


                if (action == "quit" or action == "exit" or action == "bye"\
                    or action == "sionara!"):
                        exit(0)

                if (action == "c" or action == "C" or action == "character" or action == "status"):
                        response = str(character)

                words = action.split()

                if (len(words) == 2):
                        verb = words[0]
                        noun = words[1]

                        if (verb == "go"):
                                response = "Invalid input."
                                if hasattr(Game.currentRoom, 'exits'):
                                    if (noun in Game.currentRoom.exits):
                                            Game.currentRoom =\
                                                Game.currentRoom.exits[noun]
                                            response = "Exited."

                                if hasattr(Game.currentRoom, 'rooms'):
                                    if (noun in Game.currentRoom.rooms):
                                            Game.currentRoom = \
                                                Game.currentRoom.rooms[noun]

                                            response = "Room changed."

                                if hasattr(Game.currentRoom, 'hallways'):
                                    if (noun in Game.currentRoom.hallways):
                                            Game.currentRoom =\
                                                Game.currentRoom.hallways[noun]

                                            response = "Hallway changed."

                        elif (verb == "look"):
                                response = "I don't see that item."

                                if (noun in Game.currentRoom.items):
                                        response = Game.currentRoom.items[noun]

                        elif (verb == "take"):
                                response = "I don't see that item."

                                for grabbable in Game.currentRoom.grabbables:
                                        if (noun == grabbable):
                                                Game.inventory.append(grabbable)
                                                Game.currentRoom.delGrabbable(grabbable)
                                                response = "Item grabbed."
                                                break

                        elif (verb == "equip"):
                                response = "You cannot equip that"
                                for item in Game.inventory:
                                        for i in range(len(self.grabbables)):
                                                # find the matching inventory name in list of
                                                # grabbable items
                                                if item == self.grabbables[i].name:
                                                        # if the match see if it is equippable and see if
                                                        # it has already been equipped or not
                                                        if (self.grabbables[i].equippable == True and self.grabbables[i].equipped == False):
                                                                character.strength += self.grabbables[i].strength
                                                                character.agility += self.grabbables[i].agility
                                                                response = "Item equipped"
                                                                # remove grabbable from list so it can't
                                                                # be equipped again to raise stats
                                                                del self.grabbables[i]
                                                                break
                                                        

                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)
