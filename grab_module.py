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
