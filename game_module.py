from Tkinter import *
from modules import *
from config import *
from time import sleep
import Descriptions
import Events

WIDTH = 1280
HEIGHT = 720

class Game(Frame):
        robot_currentLoc = None
        currentLoc = None
        def __init__(self, parent):
                Frame.__init__(self, parent)
                # list to keep track of all the rooms
                self.rooms = []
                # list to keep track of all the grabbables
                self.grabbables = []
                # variables to keep track of victory/lose conditions
                self.death = False
                self.victory = False

        # function to create a charact GUI implementation
        def createCharacter(self):
                global character
                # test character, finished function will implement the GUI and allow for 
                # customization
                character = Character("Student")


        def createRooms(self):
                # create the rooms and give them meaningful names
                exit_1 = Room("Exit 1", "1", "", True)
                exit_2 = Room("Exit 2", "2", "", True)
                exit_3 = Room("Exit 3", "3", "", True)
                exit_4 = Room("Exit 4", "4", "", True)
                exit_5 = Room("Exit 5", "5", "", True)
                exit_6 = Room("Exit 6", "6", "", True)

                hallway_1 = Hallway("Hallway 1", "107", "gifs/hallway1.gif")
                hallway_1.addItem("empty_chairs", Descriptions.empty_chairs)
                hallway_1.addItem("pictures", Descriptions.pictures)
                hallway_1.addExit("exit_4", exit_4)

                hallway_2 = Hallway("Hallway 2", "112", "gifs/hallway2.gif")
                hallway_2.addItem("empty_chairs", Descriptions.empty_chairs)
                hallway_2.addItem("fire_alarm", Descriptions.fire_alarm)
                hallway_2.addExit("exit_3", exit_3)

                hallway_3 = Hallway("Hallway 3", "131", "gifs/hallway3.gif")
                hallway_3.addItem("empty_chairs", Descriptions.empty_chairs)
                hallway_3.addExit("exit_1", exit_1)
                hallway_3.addExit("exit_2", exit_2)

                hallway_4 = Hallway("Hallway 4", "150", "gifs/hallway4.gif")
                hallway_4.addItem("empty_chairs", Descriptions.empty_chairs)
                hallway_4.addExit("exit_5", exit_5)

                hallway_5 = Hallway("Hallway 5", "161", "gifs/hallway5.gif")
                hallway_5.addItem("empty_chairs", Descriptions.empty_chairs)
                hallway_5.addExit("exit_6", exit_6)

                hallway_1.addHallway("hallway_2", hallway_2)
                hallway_2.addHallway("hallway_1", hallway_1)
                hallway_2.addHallway("hallway_3", hallway_3)
                hallway_3.addHallway("hallway_2", hallway_2)
                hallway_3.addHallway("hallway_4", hallway_4)
                hallway_4.addHallway("hallway_3", hallway_3)
                hallway_4.addHallway("hallway_5", hallway_5)
                hallway_5.addHallway("hallway_4", hallway_4)


                _160 = Room("Classroom", "160", "gifs/160.gif", True)
                _160.addItem("desks", Descriptions.desks)
                _160.addItem("chairs", Descriptions.chairs)
                _160.addExit("hall", hallway_5)

                _158 = Room("Classroom", "158", "gifs/158.gif", True)
                _158.addExit("hall", hallway_5)

                _157 = Room("Machine Vision/AI (Robotics Lab)", "157", "gifs/157.gif", True)
                _157.addItem("frequency_inhibitor", Descriptions.inhibitor)
                _157.addGrabbable("frequency_inhibitor")
                _157.addExit("hall", hallway_5)

                _156 = Room("Classroom", "156", "gifs/156.gif")
                _156.addExit("hall", hallway_5)

                _155 = Room("Dr. Ibrahim Abdoulahi's Office", "155", "gifs/155.gif")
                _155.addItem("pictures", Descriptions.pictures)
                _155.addExit("hall", hallway_5)

                _154 = Room("Classroom", "149", "gifs/149.gif", True)
                _154.addExit("hall", hallway_5)

                _153 = Room("Classroom", "153", "gifs/153.gif")
                _153.addItem("desks", Descriptions.desks)
                _153.addItem("chairs", Descriptions.chairs)
                _153.addExit("hall", hallway_5)

                _152 = Room("Bathroom", "152", "gifs/152.gif")
                _152.addItem("toilet_paper", Descriptions.toilet_paper)
                _152.addItem("dirty_sinks", Descriptions.dirty_sinks)
                _152.addExit("hall", hallway_5)

                _151 = Room("Optoelectronics Lab", "151", "gifs/151.gif")
                _151.addItem("desks", Descriptions.desks)
                _151.addItem("chairs", Descriptions.chairs)
                _151.addExit("hall", hallway_4)

                _149 = Room("Dr. Miguel Gates' Office", "149", "gifs/149.gif")
                _149.addExit("hall", hallway_4)
                _149.addItem("gates_desk", Descriptions.gates_desk)
                _149.addItem("gates_books", Descriptions.gates_books)

                _148 = Room("Storage", "148" , "gifs/148.gif")
                _148.addExit("hall", hallway_4)
                _148.addItem("piles_of_junk", Descriptions.piles_of_junk)

                _147 = Room("Dr. Andrey Timofeyev's Office", "147", "gifs/147.gif")
                _147.addItem("key", Descriptions.key)
                _147.addItem("andreys_desk", Descriptions.andres_desk)
                _147.addItem("andreys_computer ", Descriptions.andres_computer)
                _147.addGrabbable("key")
                _147.addExit("hall", hallway_4)

                _146 = Room("Classroom", "146" , "gifs/146.gif", True)
                _146.addExit("hall", hallway_4)
                _146.addItem("desks", Descriptions.desks)
                _146.addItem("chairs", Descriptions.chairs)

                _145 = Room("Classroom", "145", "gifs/145.gif")
                _145.addExit("hall", hallway_4)
                _145.addItem("desks", Descriptions.desks)
                _145.addItem("chairs", Descriptions.chairs)

                _144 = Room("Computer Lab", "144", "gifs/144.gif")
                _144.addExit("hall", hallway_4)
                _144.addItem("computers", Descriptions.computers)
                _144.addItem("chairs", Descriptions.chairs)

                _143 = Room("Unoccupied Office", "143", "gifs/143.gif", True)
                _143.addExit("hall", hallway_4)
                _143.addItem("walls", Descriptions.walls)

                _142 = Room("The Grid", "142", "gifs/142.gif")
                _142.addExit("hall", hallway_4)
                _142.addItem("chained_power_strips", Descriptions.chained_power_strips)
                _142.addItem("couches", Descriptions.couches)
                _142.addItem("paintintgs", Descriptions.paintings)

                _141 = Room("Charlotte Wilkerson's Office", "141", "gifs/141.gif")
                _141.addExit("hall", hallway_4)
                _141.addItem("wilkersons_desk", Descriptions.wilkersons_desk)
                _141.addItem("wilkersons_pictures", Descriptions.wilkersons_pictures)

                _140 = Room("Big Classroom", "140", "gifs/140.gif")
                _140.addExit("hall", hallway_3)
                _140.addItem("desks", Descriptions.desks)
                _140.addItem("chairs", Descriptions.chairs)

                _138 = Room("Storage", "138", "gifs/138.gif", True)
                _138.addExit("hall", hallway_3)
                _138.addItem("piles_of_junk", Descriptions.piles_of_junk)

                _136 = Room("Conference Room", "136", "gifs/136.gif")
                _136.addExit("hall", hallway_3)
                _136.addItem("table", Descriptions.table)
                _136.addItem("the_chairs", Descriptions.the_chairs)

                _134 = Room("Faculty Bathroom", "134", "gifs/134.gif")
                _134.addExit("hall", hallway_3)
                _134.addItem("toilet_paper", Descriptions.toilet_paper)
                _134.addItem("dirty_sink", Descriptions.dirty_sink)
                _134.addGrabbable("dirty_sink")

                _132 = Room("Bathroom", "132", "gifs/132.gif")
                _132.addExit("hall", hallway_3)
                _132.addItem("toilet_paper", Descriptions.toilet_paper)
                _132.addItem("dirty_sinks", Descriptions.dirty_sinks)

                _130 = Room("Janitor" , "130", "gifs/130.gif", False)
                _130.addItem("janitor_keys", Descriptions.keys)
                _130.addItem("cleaning_supplies", Descriptions.cleaning_supplies)
                _130.addGrabbable("janitor_keys")
                _130.addExit("hall", hallway_3)

                _128 = Room("Bathroom", "128", "gifs/128.gif")
                _128.addItem("writing_on_the_walls", Descriptions.writing_on_the_walls)
                _128.addItem("vacant_stall", Descriptions.vacant_stall)
                _128.addItem("toilet_paper", "")
                _128.addGrabbable("toilet_paper")
                _128.addExit("hall", hallway_3)

                _127 = Room("Dean Waiting Room", "127", "gifs/127.gif")
                _127.addExit("hall", hallway_2)
                _127.addItem("more_chairs", Descriptions.more_chairs)

                _125 = Room("Office", "125", "gifs/125.gif", True)
                _125.addExit("hall", hallway_2)
                _125.addItem("walls", Descriptions.walls)

                _123 = Room("Office", "123", "gifs/123.gif")
                _123.addExit("hall", hallway_2)
                _123.addItem("walls", Descriptions.walls)

                _122 = Room("Classroom", "122", "gifs/122.gif")
                _122.addExit("hall", hallway_2)
                _122.addItem("desks", Descriptions.desks)
                _122.addItem("chairs", Descriptions.chairs)

                _121 = Room("Dr. Galen E. Turner's Office", "121", "gifs/121.gif", True)
                _121.addExit("hall", hallway_2)
                _121.addItem("turners_desk", Descriptions.turners_desk)
                _121.addItem("turners_book_shelves", Descriptions.turners_book_shelves)

                _120 = Room("Classroom", "120", "gifs/120.gif")
                _120.addExit("hall", hallway_2)
                _120.addItem("desks", Descriptions.desks)
                _120.addItem("chairs", Descriptions.chairs)

                _119 = Room("Dr. Ben Choi's Office", "119", "gifs/119.gif")
                _119.addExit("hall", hallway_2)
                _119.addItem("chois_desk", Descriptions.chois_desk)
                _119.addItem("chois_couch", Descriptions.chois_couch)

                _118 = Room("Storage", "118", "gifs/118.gif")
                _118.addExit("hall", hallway_2)
                _118.addItem("piles_of_junk", Descriptions.piles_of_junk)

                _117 = Room("Dr. Ben Drozdenso's Office", "117", "gifs/117.gif")
                _117.addExit("hall", hallway_2)
                _117.addItem("drozdensos_books", Descriptions.drozdensos_books)
                _117.addItem("drozdensos_desk", Descriptions.drozdensos_desk)

                _115 = Room("Dr. Michael O'Neal's Office", "115", "gifs/115.gif")
                _115.addExit("hall", hallway_2)
                _115.addItem("oneals_desk", Descriptions.oneals_desk)
                _115.addItem("oneals_book_shelves", Descriptions.oneals_book_shelves)

                _113 = Room("Office Extension", "113", "gifs/113.gif")
                _113.addExit("hall", hallway_2)
                _113.addItem("lots_of_chairs", Descriptions.lots_of_chairs)

                _111 = Room("Unoccupied Office", "111", "gifs/111.gif", True)
                _111.addExit("hall", hallway_2)
                _111.addItem("walls", Descriptions.walls)

                _107 = Room("Secret Torture Room", "107", "gifs/107.gif", True)

                _106 = Room("Instrument Room", "106", "gifs/106.gif")
                _106.addExit("hall", hallway_1)
                _106.addItem("desks", Descriptions.desks)
                _106.addItem("chairs", Descriptions.chairs)

                _105 = Room("Classroom", "105", "gifs/105.gif")
                _105.addItem("andrey", Descriptions.andre)
                _105.addItem("cart", Descriptions.cart)
                _105.addItem("spare_parts", Descriptions.spare_parts)
                _105.addItem("the_white_board", Descriptions.the_white_board)
                _105.addItem("sticky_note", Descriptions.note)
                _105.addGrabbable("sticky_note")
                _105.addExit("hall", hallway_1)

                _104 = Room("Power System Labs", "104", "gifs/104.gif")
                _104.addExit("hall", hallway_1)
                _104.addItem("piles_of_junk", Descriptions.piles_of_junk)

                _103 = Room("Machinary Classroom", "103", "gifs/103.gif")
                _103.addExit("hall", hallway_1)
                _103.addItem("big_machines", Descriptions.big_machines)

                _102 = Room("Electrical Distribution", "102", "gifs/102.gif")
                _102.addExit("hall", hallway_1)
                _102.addItem("fuses", Descriptions.fuses)

                _101 = Room("Data Mining Lab", "101", "gifs/101.gif")
                _101.addExit("hall", hallway_1)
                _101.addItem("computers", Descriptions.computers)

                _100 = Room("Power Systems Lab", "100", "gifs/100.gif")
                _100.addExit("hall", hallway_1)
                _100.addItem("piles_of_junk", Descriptions.piles_of_junk)


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
                hallway_3.addRoom("130", _130)
                hallway_3.addRoom("132", _132)
                hallway_3.addRoom("134", _134)
                hallway_3.addRoom("136", _136)
                hallway_3.addRoom("138", _138)
                hallway_3.addRoom("140", _140)

                hallway_4.addRoom("141", _141)
                hallway_4.addRoom("142", _142)
                hallway_4.addRoom("143", _143)
                hallway_4.addRoom("144", _144)
                hallway_4.addRoom("145", _145)
                hallway_4.addRoom("146", _146)
                hallway_4.addRoom("147", _147)
                hallway_4.addRoom("148", _148)
                hallway_4.addRoom("149", _149)
                hallway_4.addRoom("151", _151)

                hallway_5.addRoom("152", _152)
                hallway_5.addRoom("153", _153)
                hallway_5.addRoom("154", _154)
                hallway_5.addRoom("155", _155)
                hallway_5.addRoom("156", _156)
                hallway_5.addRoom("157", _157)
                hallway_5.addRoom("158", _158)
                hallway_5.addRoom("160", _160)

 
                Game.currentLoc = _128
                Game.robot_currentLoc = _157
                Game.inventory = []

        def setupGUI(self):
                self.pack(fill=BOTH, expand=1)
                Game.player_input = Entry(self, bg="white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side=BOTTOM, fill=X)
                Game.player_input.focus()

                img = None
                Game.image = Label(self, bg="white", width=1274, height=660, anchor=CENTER, image=img)
                Game.image.image = img
                Game.image.pack(side=LEFT, fill=Y)
                Game.image.pack_propagate(False)

                text_frame = Frame(self, width=WIDTH / 2)
                Game.text = Text(text_frame, bg="lightgrey", state=DISABLED, font=("Courier New", 18))
                Game.text.tag_configure("sysfix", font="Fixedsys")
                Game.text.pack(fill=Y, expand=1)
                text_frame.pack(side=RIGHT, fill=Y)
                text_frame.pack_propagate(False)

        def setRoomImage(self):
                Game.img = PhotoImage(file=Game.currentLoc.image)

                Game.image.config(image=Game.img)
                Game.image.image = Game.img

        

        def setStatus(self, status):
                global character
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0", END)
                Game.text.insert(END, str(Game.currentLoc))
                Game.text.insert(END, "\n\nYou are carrying: ")
                Game.text.insert(END, str(Game.inventory) + "\n\n")
                Game.text.insert(END, status)
                #typeit(Game.text, END, str(status))
                Game.text.config(state=DISABLED)
        
                      
                      
        def play(self):
                self.createCharacter()
                self.createRooms()
                self.setupGUI()
                self.setRoomImage()
                # set status with intro
                self.setStatus(Events.intro)

        def inventory(self):
            print "test"
            if inv_status == False:
                Game.text2.insert(INSERT, Game.text.get("1.0", "end-1c"))
                Game.text.delete("1.0", END)
                Game.text.insert(END, "test")
            else:
                Game.text.insert(INSERT, Game.text2.get("1.0", "end-1c"))

            '''Game.text.config(state=NORMAL)
            Game.text.delete("1.0", END)
            Game.setStatus("You are carrying: ")
            '''



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

                if (action == "clear"):
                        response = ""

                words = action.split()

                if (len(words) == 2):
                        verb = words[0]
                        noun = words[1]

                        if (verb == "go"):
                                response = "Invalid input. Please provide a valid exit, room, or hallway."
                                if hasattr(Game.currentLoc, 'exits'):
                                        if (noun in Game.currentLoc.exits):
                                                if not Game.currentLoc.exits.get(noun).locked:
                                                        Game.currentLoc = Game.currentLoc.exits[noun]

                                                elif "janitor_keys" in Game.inventory:
                                                        if Game.currentLoc.exits[noun].number == "6":
                                                                Game.currentLoc = Game.currentLoc.exits[noun]
                                                                response = "The key unlocked the door. Exited."

                                                        response = "Exited."
                                                else:
                                                      response = "{} is locked.".format(Game.currentLoc.exits.get(noun).name)   

                                if hasattr(Game.currentLoc, 'rooms'):
                                        if (noun in Game.currentLoc.rooms):
                                                if not Game.currentLoc.rooms.get(noun).locked:
                                                        Game.currentLoc = Game.currentLoc.rooms[noun]

                                                        response = "Room changed."
                                                        
                                                elif "key" in Game.inventory:
                                                        if Game.currentLoc.rooms[noun].number == "157":
                                                                Game.currentLoc = Game.currentLoc.rooms[noun]
                                                                response = "The key unlocked the door. Room changed."


                                                else:
                                                        response = "{} is locked.".format(Game.currentLoc.rooms.get(noun).name)

                                if hasattr(Game.currentLoc, 'hallways'):
                                        if (noun in Game.currentLoc.hallways):
                                                Game.currentLoc = Game.currentLoc.hallways[noun]

                                                response = "Hallway changed."

                        elif (verb == "look"):
                                response = "Item not found."

                                if (noun in Game.currentLoc.items):
                                        response = Game.currentLoc.items[noun]

                        elif (verb == "take"):
                                response = "Item not found."

                                for grabbable in Game.currentLoc.grabbables:
                                        if (noun == grabbable):
                                                Game.inventory.append(grabbable)
                                                Game.currentLoc.delGrabbable(grabbable)
                                                response = "Item grabbed."
                                                break

                        elif (verb == "equip"):
                                response = "You cannot equip that."
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
                        elif (verb == "about"):
                                response = "Unknown room, exit, or item given."
                                if hasattr(Game.currentLoc, 'rooms'):
                                        response = ""
                                        if noun == "all":
                                                for key, value in Game.currentLoc.rooms.iteritems():
                                                        response += key + "\t" + value.name + "\n"

                                        if (noun in Game.currentLoc.rooms):
                                                response = "Room {}: {}".format(Game.currentLoc.rooms[noun].number, Game.currentLoc.rooms[noun].name)

                                if (noun in Game.inventory):
                                        desc = getattr(Descriptions, noun)
                                        response = "'{}': {}".format(noun, desc)


                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)
