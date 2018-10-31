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
