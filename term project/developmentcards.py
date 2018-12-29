# please decide how these classes will let you do things with them....
from board import *
from player import *
class DevelopmentCard(object):
    pass
    # figure out what this class is going to be doing

class Knight(DevelopmentCard):
    def __init__(self, type):
        self.type = type
    # allows you to move the robber
    # robber will be a hard thing to do
    def play(self):
        pass
    
class VictoryPoint(DevelopmentCard):
    def __init__(self, type):
        self.type = type
    # adds victory point to points
    #  once you add points this will be an easy boi
    def play(self):
        pass

class Monopoly(DevelopmentCard):
    def __init__(self, type):
        self.type = type
    # allows you to take other player's cards
    # might be a little ocmplicated
    def play(self):
        pass
    
class YearOfPlenty(DevelopmentCard):
    def __init__(self, type):
        self.type = type
    # allows you to pick 2 resources from bank
    # this will open up in a new window
    def play(self):
        pass
    
class RoadBuilding(DevelopmentCard):
    def __init__(self, type):
        self.type = type
    # when you want to play this card it will add 2 wood and 2 brick to what you have
    # no it will literally just add 2 roads to the building pile
    def play(self):
        pass
        
# have to figure out how to make them interact with each other???
        