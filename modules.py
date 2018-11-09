def typeit(widget, index, string):
        if len(string) > 0:
                widget.insert(index, string[0])
                if len(string) > 1:
                        # compute index of next char
                        index = widget.index("%s + 1 char" % index)

                        # type the next character in half a second
                        widget.after(100, typeit, widget, index, string[1:])

class Grabbables(object):
        # grabbables are items that can be added to the players inventory
        # they will have a name a description and attribute modifiers
        # they will also have variables for whether or not it is equippable/equipped
        def __init__(self, name, desc):
                self.name = name
                self.desc = desc
                
        # getters and setters for instance variables
        @property
        def name(self):
                return self._name
        @name.setter
        def name(self, value):
                self._name = value
            
        @property
        def desc(self):
                return self._desc
        @desc.setter
        def desc(self, value):
                self._desc = value

class Character(object):
    # character classes take a name, strength, and agility.
    # strength effects the chance of overcoming a physical struggle, agility
    # agility effects the chance of running away. Characters will also have a health
    # variable and when that reaches 0 the player losses the game.
    def __init__(self, name):
        self.name = name

    # getters and setters for the character class
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # string function that will display all character information
    def __str__(self):
        return "Name: {}".format(self.name)

class Room(object):
        # the constructor
        def __init__(self, name, number, image, locked = False):
            # rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
            # items (e.g., table), item descriptions (for each item), and grabbables (things that can
            # be taken into inventory)
            self.name = name
            self.number = number
            self.image = image
            self.exits = {}
            self.items = {}
            self.grabbables = []
            self.locked = locked

        # getters and setters for the instance variables
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def number(self):
            return self._number

        @number.setter
        def number(self, value):
            self._number = value

        @property
        def image(self):
            return self._image

        @image.setter
        def image(self, value):
            self._image = value

        @property
        def exits(self):
            return self._exits

        @exits.setter
        def exits(self, value):
            self._exits = value

        @property
        def items(self):
            return self._items

        @items.setter
        def items(self, value):
            self._items = value

        @property
        def grabbables(self):
            return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
            self._grabbables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
            # append the exit and room to the appropriate dictionary
            self._exits[exit] = room

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
            # append the item and description to the appropriate dictionary
            self._items[item] = desc

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
            # append the item to the list
            self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
            # remove the item from the list
            self._grabbables.remove(item)

        # returns a string description of the room
        def __str__(self):
            # first, the room name
            s = "You are in the {}.\n".format(self.name)

            # next, the items in the room
            s += "You see: "
            for item in self.items.keys():
                s += item + " "
            s += "\n\n"

            # next, the exits from the room
            s += "Exits: "
            for exit in self.exits.keys():
                s += "\n" + "- " + exit

            return s


class Hallway(Room):
    def __init__(self, name, number, image):
        Room.__init__(self, name, number, image)
        self.rooms = {}
        self.hallways = {}

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    @property
    def hallways(self):
        return self._hallways

    @hallways.setter
    def hallways(self, value):
        self._hallways = value


    def addRoom(self, number, room):
        self._rooms[number] = room

    def addHallway(self, name, hallway):
        self._hallways[name] = hallway

    def __str__(self):
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n\n"

        s += "Rooms: "
        keys = iter(sorted(self.rooms.keys()))
        for key in keys:
            next_key = next(keys)
            if next_key:
                s += "\n" + key + "    " + next_key
            else:
                s += "\n" + key
        s += "\n\n"

        # next, the hallways next to the current hallway
        s += "Hallways: "
        for hallway in self.hallways.keys():
            s += "\n" + "- " + hallway

        s += "\n\n"

        # next, the exits from the hallway
        s += "Exits: "
        for exit in self.exits.keys():
            s += "\n" + "- " + exit

        return s
