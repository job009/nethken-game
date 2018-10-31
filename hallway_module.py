from room_module import Room

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
