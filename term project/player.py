from board import *
class player(object):
    def __init__(self, color):
        self.color = color
        self.roads = ["road"] * 15
        self.settlements = ["settlement"] * 5
        self.cities = ["cities"] * 4
        self.points = 0
        self.brick = 20
        self.ore = 20
        self.wheat = 20
        self.sheep = 20
        self.wood = 20
        self.knightsPlayed = 0
        # resources list should be appended when playing the game
        self.resources = {}
        self.cards = []
        # self.resources is a list which holds the numbers and what player gets if num is rolled
        self.roadsBought = 0
        self.settlementsBought = 0
        self.citiesBought = 0
        self.scount = 0
        self.rcount = 0
        self.isFirst = True

        

    def drawRoad(self):
        if self.roads != [] and self.roadsBought >= 1:
            self.roads.remove("road")
            self.roadsBought -= 1
            # in order to build road must click on 2 coordinates which must
            # be next to each other
    
    def drawSettlement(self):
        if self.settlements != [] and self.settlementsBought >= 1:
            self.settlements.remove("settlement")
            self.settlementsBought -= 1
            self.points += 1
        
    def drawCity(self):
        if self.cities!= [] and self.citiesBought >= 1:
            self.settlements.append("settlement")
            self.cities.remove("cities")
            self.citiesBought -= 1
            self.points += 1
        
    def pickedVP(self):
        self.points += 1
        
    def buyRoad(self):
        if self.brick >= 1 and self.wood >= 1 and self.roads != []:
            self.brick -= 1
            self.wood -= 1
            self.roadsBought += 1
            return True
        return None
            # add road to list of roads and then build road under road class
    
    def buySettlement(self):
        if self.brick >= 1 and self.wood >= 1 and self.sheep >= 1 and self.wheat >= 1 and self.settlements != []:
            self.brick -= 1
            self.wood -= 1
            self.sheep -= 1
            self.wheat -= 1
            self.settlementsBought += 1
            return True
        return None
            # add settlement to list of settlements and then build using settlement class (basically draw it)
            
    def buyCity(self):
        if self.ore >= 2 and self.wheat >= 3 and self.cities != []:
            self.ore -= 2
            self.wheat -= 3
            self.citiesBought += 1
            return True
        return None
            # add city to list and then build using class!
    
    def buyDVC(self):
        if self.ore >= 1 and self.sheep >= 1 and self.wheat >= 1:
            self.ore -= 1
            self.sheep -= 1
            self.wheat -= 1
        return None
    
    def playKnight(self):
        self.dvCards.remove("knight")
        self.knightsPlayed += 1
    
    def win(self, other):
        p1 = self.knightsPlayed
        p2 = other.knightsPlayed
        if p1 >= p2 and p1 >= 3: 
            self.points += 2
            if self.points >= 8:
                return True
        elif self.points >= 8:
             return True
        return False
    
    def canTrade(self):
        if self.brick >= 4 or self.wheat >= 4 or self.sheep >= 4 or self.ore >= 4 or self.wood >= 4:
            return True
        
class Road(object):
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = 5
        
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
        fill = self.color, width = self.width)
        
class City(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 15
        
    def draw(self, canvas):
        points = [(self.x - self.size, self.y + self.size), (self.x + self.size, \
        self.y + self.size), (self.x + self.size, self.y - self.size), (self.x, self.y - self.size),\
            (self.x, self.y), (self.x - self.size, self.y) ]
        canvas.create_polygon(points, fill = self.color, outline = "black")
        
class Settlement(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = 10
        self.color = color
        
    def __hash__(self):
        return hash((self.x, self.y, self.color))
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.color == other.color
        
    def __repr__(self):
        return "settlement at (%d, %d) and color: %s" % (self.x, self.y, self.color)
        
    def draw(self, canvas):
        points = [(self.x - self.size, self.y + self.size),(self.x + self.size, self.y + self.size)\
        ,(self.x + self.size, self.y - self.size),(self.x, self.y - 2* self.size),(self.x - self.size, self.y\
         - self.size)]
        canvas.create_polygon(points, fill = self.color, outline = "black")
        
class RobberPiece(object):
    def __init__(self, x, y, size, tileSize, cX, cY):
        self.x = cX + (1.5 * x * size)
        self.y = cY + (2 * y * tileSize)
        self.size = 15
        self.sze = size
        self.tileSize = tileSize
        self.cX = cX
        self.cY = cY
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill = "black")
        
    def move(self, x, y):
        self.x = self.cX + (1.5 * x * self.size)
        self.y = self.cY + (2 * y * self.tileSize)
        
        
        
        
        