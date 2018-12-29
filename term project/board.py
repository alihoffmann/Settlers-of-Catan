# code for board class is modelled form this repository https://gist.github.com/sareon/1365808
import random
import math
from player import *
# list of all possible numbers, randomizes location
nums = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

# inititates colors
CLAY = "firebrick4"
ORE = "gray40"
WHEAT = "khaki3"
SHEEP = "SpringGreen2"
WOOD = "tan4"
SAND = "wheat1"

# locations of every hexTile
# redoHexTiles using more of a rectangular grid and radians / circles
hexTiles = [(0,1), (0,-1), (-1,0.5), (-1,-0.5), (1,0.5), (1,-0.5), (2,0), (-2,0), (0,2), (0,-2), (1,1.5), (1,-1.5), (-1,1.5), (-1, -1.5), (2,1), (2,-1), (-2,1), (-2,-1)]


# inititates variables with types
resource = {CLAY: 'brick', ORE: 'ore', WHEAT: 'wheat', SHEEP: 'sheep', WOOD: 'wood', SAND: 'Desert, Nothing'}

hexResources = [CLAY, CLAY, CLAY, ORE, ORE, ORE, WHEAT, WHEAT, WHEAT, WHEAT, SHEEP, SHEEP, SHEEP, SHEEP, WOOD, WOOD, WOOD, WOOD]

newHex = []
for i in range(len(hexResources)):
    newHex += [(hexResources[i], nums[i])]

# sets up a list of resources with their numbers and then randomizes it
random.shuffle(newHex)
random.shuffle(newHex)

def rounds(num):
    n = num % 1
    if n >= 0.5:
        return int(num // 1) + 1
    return int(num // 1)

class Board(object):

    def __init__(self, size, data):
        self.cX = data.width // 2
        self.cY = 3 * data.height / 5
        self.tileSize = 0.866 * size
        self.tiles = []
        self.settlements = []
        self.size = size
        # sets up deck of development cards
        self.cards = ["knight"] * 14
        self.cards += ["VP"] * 5
        self.cards += ["RB"] * 2
        self.cards += ["mon"] * 2
        self.cards += ["YOP"] * 2
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        # links actual points to surrounding hex blocks FILLED
        self.hexNum = {}
        # links actual points to a name using hex number and nums 0-6 
        # each point will be given only one name and then :))
        # pTN - point to name
        self.pTN = {}
        # links each hex tile to a number and to a type of resource --> create this with zipped code and stuff
        self.tileNum = {}
        # links given name to all adjacent points --> makes it easier to check adjacent for making settlements --> harcode this please
        self.adjPnts = {
    (-1, 1.5, 2): [(-1, 1.5, 3), (-2, -1, 3), (0, 0, 5)], 
    (0, 0, 5): [(-1, 1.5, 2), (0, 0, 4), (0, 0, 0)],
    (0, 0, 4): [(0, 0, 5), (0, 0, 3), (1, 1.5, 1)],
    (1, 1.5, 1): [(0, 0, 4), (1, 1.5, 0), (2, 1, 0)],
    (1, 1.5, 0): [(1, 1.5, 0), (-1, 1.5, 3), (1, 1.5, 5)],
    (-1, 1.5, 3): [(1, 1.5, 0), (-1, 1.5, 4), (-1, 1.5, 2)],
    (-1, -1.5, 4): [(-1, -1.5, 3), (-2, -1, 3), (0, 0, 1)],
    (-1, -1.5, 3): [(-1, -1.5, 4), (1, -1.5, 0), (-1, -1.5, 2)],
    (1, -1.5, 0): [(-1, -1.5, 3), (1, -1.5, 5), (1, -1.5, 1)],
    (1, -1.5, 5): [(1, -1.5, 0), (0, 0, 2), (2, -1, 0)],
    (0, 0, 2): [(1, -1.5, 5), (0, 0, 1), (0, 0, 3)],
    (0, 0, 1): [(0, 0, 2), (-1, -1.5, 4), (0, 0, 0)],
    (-2, 1, 2): [(-2, 0, 3), (-2, 1, 1), (-2, 1, 3)],
    (-2, 0, 3): [(-2, 1, 2), (0, 0, 0), (-2, -1, 4)],
    (0, 0, 0): [(-2, 0, 3), (0, 0, 5), (0, 0, 1)],
    (-2, 1, 3): [(-1, 1.5, 2), (-2, 1, 4), (-2, 1, 1)],
    (-2, -1, 4): [(-2, 1, 5), (-2, -1, 3), (-2, 0, 3)],
    (-2, -1, 3): [(-2, -1, 4), (-2, -1, 2), (-1, -1.5, 4)],
    (0, 0, 3): [(0, 0, 2), (0, 0, 4), (2, 0, 0)],
    (2, 0, 0): [(0, 0, 3), (2, -1, 5), (2, 1, 1)],
    (2, 1, 1): [(2, 0, 0), (2, 1, 2), (2, 1, 0)],
    (2, 1, 0): [(2, 1, 1), (2, 1, 5), (1, 1.5, 1)],
    (2, -1, 0): [(2, -1, 5), (2, -1, 1), (1, -1.5, 5)],
    (2, -1, 5): [(2, -1, 0), (2, -1, 4), (2, 0, 0)],
    (2, -1, 4): [(2, -1, 5), (2, -1, 3), (2, 0 , 3)],
    (2, 0, 3): [(2, -1, 4), (2, 1, 2)],
    (2, 1, 2): [(2, 0 , 3), (2, 1, 1), (2, 1, 3)],
    (-2, 0, 0): [(-2, -1, 5), (-2, 1, 1)],
    (-2, -1, 5): [(-2, -1, 4), (-2, -1, 0)],
    (-2, 1, 1): [(-2, 1, 0), (-2, 1, 2), (-2, 0, 0)],
    (-1, 1.5, 4): [(-1, 1.5, 3), (-1, 1.5, 5), (0, 2, 5)],
    (1, 1.5, 5): [(1, 1.5, 4), (0, 2, 4), (1, 1.5, 0)],
    (0, 2, 4): [(1, 1.5, 5), (0, 2, 5)],
    (0, 2, 5): [(0, 2, 4), (-1, 1.5, 4)],
    (-1, -1.5, 2): [(-1, -1.5, 1), (0, -2, 1), (1, -1.5, 0)],
    (0, -2, 1): [(0, -2, 2), (1, -1.5, 1)],
    (0, -2, 2): [(0, -2, 1), (1, -1.5, 1)],
    (1, -1.5, 1): [(0, -2, 2), (1, -1.5, 0), (1, -1.5, 2)],
    (2, 1, 5): [(2, 1, 0), (1, 1.5, 4), (2, 1, 4)],
    (1, 1.5, 4): [(2, 1, 5), (1, 1.5, 5)],
    (1, -1.5, 2): [(1, -1.5, 1), (2, -1, 1)],
    (2, -1, 1): [(1, -1.5, 2), (2, -1, 0), (2, -1, 2)],
    (-2, 1, 4): [(-2, 1, 5), (-1, 1.5, 5), (-2, 1, 3)],
    (-1, 1.5, 5): [(-2, 1, 4), (-1, 1.5, 4)],
    (-2, -1, 2): [(-2, -1, 1), (-1, -1.5, 1), (-2, -1, 3)],
    (-1, -1.5, 1): [(-2, -1, 2), (-1, -1.5, 2)],
    (2, 1, 3): [(2, 1, 4), (2, 1, 2)],
    (2, 1, 4): [(2, 1, 3), (2, 1, 5)],
    (2, -1, 2): [(2, -1, 3), (2, -1, 1)],
    (2, -1, 3): [(2, -1, 2), (2, -1, 4)],
    (-2, 1, 0): [(-2, 1, 5), (-2, 1, 1)],
    (-2, 1, 5): [(-2, 1, 0), (-2, 1, 4)],
    (-2, -1, 0): [(-2, -1, 1), (-2, -1, 5)],
    (-2, -1, 1): [(-2, -1, 2), (-2, -1, 0)]
    }
        # links given names to if they have settlements, road ends, or both
        self.filledPoints = {}
        self.tileNum[(0, 0)] = ("desert", -1)
        for tile in zip(hexTiles, newHex):
            self.tiles.append(Hex(tile[0], size, tile[1][0], tile[1][1], self))
            self.tileNum[tile[0]] = (resource[tile[1][0]], tile[1][1])
            # ensures that desert is always at the center
        self.tiles.append(Hex((0, 0), size, SAND, - 1, self))\
        
    def drawBoard(self, canvas):
        for hex in self.tiles:
            hex.drawHex(canvas)
        for settlements in self.settlements:
            settlements.drawSettlement(canvas)
            
    def buyDevCard(self):
        return self.cards.pop()
    
class Hex(object):
    def __init__(self, center, size, type, number, board):
        self.center = center
        self.x = rounds(board.cX + (1.5 * center[0] * size)) 
        self.y = rounds(board.cY + (2 * center[1] * board.tileSize)) 
        self.circSize = 15
        self.size = size
        self.type = type
        self.value = number
        self.hasRobber = False
        self.color = "black"
        
        
        # make a dictionary using the points on the grid and map it to which corner number of each hexagon
        self.points = []
        self.points.append((self.x - self.size, self.y))
        lstPoints = [(center[0], center[1])] + board.hexNum.get((self.x - self.size, self.y), [])
        board.hexNum[(self.x - self.size, self.y)] = lstPoints
        board.pTN[(self.x - self.size, self.y)] = (center[0], center[1], 0)
        
        self.points.append((self.x - (self.size/2), rounds(self.y - (0.866*self.size)) ))
        lstPoints = [(center[0], center[1])] + board.hexNum.get((self.x - (self.size/2), rounds(self.y - (0.866*self.size)) ), [])
        board.hexNum[(self.x - (self.size/2), rounds(self.y - (0.866*self.size)) )] = lstPoints
        board.pTN[(self.x - (self.size/2), rounds(self.y - (0.866*self.size)) )] = (center[0], center[1], 1)
        
        self.points.append((self.x + (self.size/2), rounds(self.y - (0.866*self.size)) ))
        lstPoints = [(center[0], center[1])] + board.hexNum.get((self.x + (self.size/2), rounds(self.y - (0.866*self.size)) ), [])
        board.hexNum[(self.x + (self.size/2), rounds(self.y - (0.866*self.size)) )] = lstPoints
        board.pTN[(self.x + (self.size/2), rounds(self.y - (0.866*self.size)) )] = (center[0], center[1], 2)
        
        self.points.append((self.x + self.size, self.y))
        lstPoints = [(center[0], center[1])] + board.hexNum.get((self.x + self.size, self.y), [])
        board.hexNum[(self.x + self.size, self.y)] = lstPoints
        board.pTN[(self.x + self.size, self.y)] = (center[0], center[1], 3)
       
        self.points.append( (self.x + (self.size/2), rounds(self.y + (0.866*self.size)) ))
        lstPoints = [(center[0], center[1])] + board.hexNum.get( (self.x + (self.size/2), rounds(self.y + (0.866*self.size)) ), [])
        board.hexNum[ (self.x + (self.size/2), rounds(self.y + (0.866*self.size)) )] = lstPoints
        board.pTN[ (self.x + (self.size/2), rounds(self.y + (0.866*self.size)) )] = (center[0], center[1], 4)
       
        self.points.append(( (self.x - (self.size/2)), rounds(self.y + (0.866*self.size)) ))
        lstPoints = [(center[0], center[1])] + board.hexNum.get( (self.x - (self.size/2), rounds(self.y + (0.866*self.size)) ), [])
        board.hexNum[( (self.x - (self.size/2)), rounds(self.y + (0.866*self.size)) )] = lstPoints
        board.pTN[( (self.x - (self.size/2)), rounds(self.y + (0.866*self.size)) )] = (center[0], center[1], 5)
        
    def drawHex(self, canvas):
        canvas.create_polygon(self.points, fill = self.type, outline = "black")
        if self.value != -1:
            canvas.create_oval(self.x - self.circSize, self.y - self.circSize, self.x + self.circSize, self.y + self.circSize, fill = "wheat1")
            if self.value in (6, 8):
                self.color = "red"
            canvas.create_text(self.x, self.y, text = self.value, fill = self.color)
            
class Die(object):
    def __init__(self):
        self.num = 1
    def rollDie(self):
        self.num = random.randint(1, 6)
        
class Button(object):
    def __init__(self, x, y, width, height, color, function, text, size, *args):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.thick = 1
        self.text = text
        self.function = function
        self.args = args
        self.size = size
        self.click = False
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = self.color, width = self.thick)
        canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, text = self.text, font = ("Arial", self.size), fill = "white")
        
    def isClicked(self):
        self.function(*self.args)
        self.thick = 7
        self.click = True
        
    def unClicked(self):
        self.thick = 1
        self.click = False
        
class hButton(object):
    def __init__(self, x, y, width, function, size, *args):
        self.x = x
        self.y = y
        self.r = width
        self.function = function
        self.args = args
        self.size = size
        self.click  = False
        self.thick = 1
        self.width = self.r
        self.height = self.r
    
    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, fill = "white", width = self.thick)
        canvas.create_text(self.x + self.r / 2, self.y + self.r / 2, text = "?", font = ("Arial", self.size, "bold"), fill = "blue")
        
    def isClicked(self):
        self.function(*self.args)
        self.thick = 7
        self.click = True
        
    def unClicked(self):
        self.thick = 1
        self.click = False

