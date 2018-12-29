# Basic Animation Framework from 112 website

from tkinter import *
from board import *
from player import *
import random

####################################
# customize these functions
####################################

def init(data):
    data.screen = "start"
    data.board = Board(60, data)
    data.devCards = data.board.cards
    data.roads = []
    data.settlements = []
    data.cities = []
    data.road = False
    data.settlement = False
    data.city = False
    data.player1 = True
    data.roll = False
    data.clicked = 0
    data.x1 = 0
    data.y1 = 0
    # list of all development cards each player has --> will be updated with each card when drawn
    data.die1 = Die()
    data.die2 = Die()
    data.totalRoll = 0
    data.robber = RobberPiece(0, 0, data.board.size, data.board.tileSize, data.board.cX, data.board.cY)
    data.p1 = player("red")
    data.p2 = player("green")
    # use data.name to fill in variable name for who is what / what is displayed
    if data.player1:
        data.name = data.p1
    else: data.name = data.p2
    data.first = data.name
    if data.name == data.p1: data.n1 = "p1"
    else: data.name = "p2"
    data.trade = False
    data.tradeButton = []
    makeTradeButton(data)
    data.traded = 0
    data.playButton = []
    makePlayButton(data)
    data.setButton = []
    makeSetButton(data)
    data.startButton = []
    makeStartButton(data)
    data.viewdvc = False
    data.dvcButton = []
    makedvcButton(data)
    data.countRoad = 0
    data.rb = False
    data.yop = False
    data.yopCard = 2
    data.yopCards = []
    makeyopCards(data)
    data.monCards = []
    makemonCards(data)
    data.mon = False
    data.learnCard = False
    data.hCard = Button(675, 160, 25, 25, "red", exit3, "X", 18, data)
    data.Instruction = Button(875, 80, 25, 25, "red", exit4, "X", 18, data)
    data.i = False
    data.wins = False

def exit4(data):
    data.i = False
    
def exit3(data):
    data.learnCard = False
    
def makemonCards(data):
    data.mbrick = Button(400, 225, 200, 50, "firebrick4", take, "Brick", 12, data, "brick")
    data.monCards += [data.mbrick]
    data.more = Button(400, 300, 200, 50, "gray40", take, "Ore", 12, data, "ore")
    data.monCards += [data.more]
    data.msheep = Button(400, 375, 200, 50, "SpringGreen4", take, "Sheep", 12, data, "sheep")
    data.monCards += [data.msheep]
    data.mwheat = Button(400, 450, 200, 50, "khaki3", take, "Wheat", 12, data, "wheat")
    data.monCards += [data.mwheat]
    data.mwood = Button(400, 525, 200, 50, "tan4", take, "Wood", 12, data, "wood")
    data.monCards += [data.mwood]
    
def take(data, type):
    if data.name == data.p1: name = data.p2
    else: name = data.p1
    if type == "brick":
        data.name.brick += name.brick
        name.brick = 0
    elif type =="ore":
        data.name.ore += name.ore
        name.ore = 0
    elif type =="sheep":
        data.name.sheep += name.sheep
        name.sheep = 0
    elif type == "wheat":
        data.name.wheat += name.wheat
        name.wheat = 0
    elif type == "wood":
        data.name.wood += name.wood
        name.wheat = 0
    data.mon = False
    data.viewdvc = False
    
def mon(data):
    if data.name.cards.count("mon") > 0 :
        data.mon = True
        data.name.cards.remove("mon")
        
    
def makedvcButton(data):
    data.exit2 = Button(775, 160, 25, 25, "red", exit2, "X", 18, data)
    data.dvcButton += [data.exit2]
    data.knight = Button(250, 300, 200, 50, "gray3", playKnight, "Play Knight!", 12, data )
    data.dvcButton += [data.knight]
    data.roadBuild = Button (250, 500, 200, 50, "brown", buildRoad2, "Play Road Building", 12, data)
    data.dvcButton += [data.roadBuild]
    data.yop = Button(550, 300, 200, 50, "gold", yop, "Play Year of Plenty", 12, data)
    data.dvcButton += [data.yop]
    data.monC = Button(550, 500, 200, 50, "maroon", mon, "Play Monopoly", 12, data)
    data.dvcButton +=[data.monC]
    data.help = hButton(225, 185, 35, hp, 23, data)
    data.dvcButton += [data.help]

def hp(data):
    data.learnCard = True
    
    
def makeyopCards(data): 
    data.ybrick = Button(400, 225, 200, 50, "firebrick4", buy, "Brick", 12, data, "brick")
    data.yopCards += [data.ybrick]
    data.yore = Button(400, 300, 200, 50, "gray40", buy, "Ore", 12, data, "ore")
    data.yopCards += [data.yore]
    data.ysheep = Button(400, 375, 200, 50, "SpringGreen4", buy, "Sheep", 12, data, "sheep")
    data.yopCards += [data.ysheep]
    data.ywheat = Button(400, 450, 200, 50, "khaki3", buy, "Wheat", 12, data, "wheat")
    data.yopCards += [data.ywheat]
    data.ywood = Button(400, 525, 200, 50, "tan4", buy, "Wood", 12, data, "wood")
    data.yopCards += [data.ywood]


def exit2(data):
    data.viewdvc = False
    data.seedvc.unClicked()

def yop(data):
    # triggers a new screen
    if data.name.cards.count("YOP") > 0:
        data.yop = True
        data.name.cards.remove("YOP")
    
def buildRoad2(data):
    if data.name.cards.count("RB") > 0:
        exit2(data)
        data.rb = True
        data.countRoad = 2
        data.road = True
        data.name.cards.remove("RB")
    
def playKnight(data):
    if data.name.cards.count("knight") > 0:
        if data.name == data.p1:
            lst = []
            lst += ["wheat"] * data.p2.wheat
            lst += ["ore"] * data.p2.ore
            lst += ["brick"] * data.p2.brick
            lst += ["wood"] * data.p2.wood
            lst += ["sheep"] * data.p2.sheep
            res = random.choice(lst)
            if res == "wheat":
                data.p2.wheat -= 1
                data.p1.wheat += 1
            elif res =="ore":
                data.p2.ore -= 1
                data.p1.ore += 1
            elif res == "brick":
                data.p2.brick -= 1
                data.p1.brick += 1
            elif res == "wood":
                data.p2.wood -= 1
                data.p1.wood += 1
            elif res == "sheep":
                data.p2.sheep -= 1
                data.p1.sheep += 1
        elif data.name == data.p2:
            lst = []
            lst += ["wheat"] * data.p1.wheat
            lst += ["ore"] * data.p1.ore
            lst += ["brick"] * data.p1.brick
            lst += ["wood"] * data.p1.wood
            lst += ["sheep"] * data.p1.sheep
            res = random.choice(lst)
            if res == "wheat":
                data.p1.wheat -= 1
                data.p2.wheat += 1
            elif res =="ore":
                data.p1.ore -= 1
                data.p2.ore += 1
            elif res == "brick":
                data.p1.brick -= 1
                data.p2.brick += 1
            elif res == "wood":
                data.p1.wood -= 1
                data.p2.wood += 1
            elif res == "sheep":
                data.p1.sheep -= 1
                data.p2.sheep += 1
        data.name.knightsPlayed += 1
        data.name.cards.remove("knight")
        data.viewdvc = False
        data.seedvc.unClicked()
    
def makeStartButton(data):
    data.play = Button(data.width / 2 - 50, data.height / 2, 100, 35, "PaleVioletRed3", start, "Play!", 12,  data)
    data.startButton += [data.play]
    data.Instructions = Button(data.width / 2 - 50, 500, 100, 35, "maroon1", instructions, "Need help?", 12, data )
    data.startButton += [data.Instructions]
    
def instructions(data):
    data.i = True
    
def start(data):
    data.screen = "playSet"
    
def makeSetButton(data):
    
    # modify code so that building a road actually works
    data.setroad = Button(387.5, 100, 100, 35, "orange", setRoad, "Buy Road", 12, data)
    data.setButton += [data.setroad]
    data.setsettlement = Button(387.5, 50, 225, 35, "green", setSettlement, "Buy Settlement", 12, data)
    data.setButton += [data.setsettlement]
    data.setDie = Button(800, 175, 75, 35, "gray", empty, "Roll Die", 12, data)
    data.setButton += [data.setDie]
    data.setTurn = (Button(900, 175, 75, 35, "gray", empty, "End Turn", 12, data))
    data.setButton += [data.setTurn]
    data.setWin = Button(800, 300, 175, 35, "gray", empty, "Declare Victory!", 12, data)
    data.setButton += [data.setWin]
    data.setcity = Button(512.5, 100, 100, 35, "gray", empty, "Buy City", 12, data)
    data.setButton += [data.setcity]
    data.setdvc = Button(387.5, 150, 225, 35, "gray", empty, "Buy Development Card", 12, data)
    data.setButton += [data.setdvc]
    data.setTrading = Button(800, 490, 175, 35, "gray", empty, "Trade with the bank!", 12, data)
    data.setButton += [data.setTrading]
    data.setseedvc = Button (800, 540, 175, 35, "gray", empty, "See Development Cards", 12, data)
    data.setButton += [data.setseedvc]
    
def empty(data):
    pass

    
def makePlayButton(data):
    data.prollDie = Button(800, 175, 75, 35, "blue", rollDie, "Roll Die", 12, data)
    data.playButton += [data.prollDie]
    data.endTurn = (Button(900, 175, 75, 35, "green", endTurnNow, "End Turn", 12, data))
    data.playButton += [data.endTurn]
    data.win = Button(800, 300, 175, 35, "black", win, "Declare Victory!", 12, data)
    data.playButton += [data.win]
    data.psettlement = Button(387.5, 50, 225, 35, "green", buildSettlement, "Buy Settlement", 12, data)
    data.playButton += [data.psettlement]
    # modify code so that building a road actually works
    data.proad = Button(387.5, 100, 100, 35, "orange", buildRoad, "Buy Road", 12, data)
    data.playButton += [data.proad]
    data.pcity = Button(512.5, 100, 100, 35, "purple", buildCity, "Buy City", 12, data)
    data.playButton += [data.pcity]
    data.pdvc = Button(387.5, 150, 225, 35, "indigo", buyDVC, "Buy Development Card", 12, data)
    data.playButton += [data.pdvc]
    data.trading = Button(800, 490, 175, 35, "green1", trading, "Trade with the bank!", 12, data)
    data.playButton += [data.trading]
    data.seedvc = Button (800, 540, 175, 35, "blue3", seedvc, "See Development Cards", 12, data)
    data.playButton += [data.seedvc]
    
def seedvc(data):
    data.viewdvc = True
    
def trading(data):
    if data.name.canTrade():
        data.trade = True

def win(data):
    if data.name == data.p1:
        if data.name.win(data.p2):
            data.screen = "win"
            data.winner = "Player 1"
            data.wins = True
        else: 
            data.screen = "play"
            data.win.unClicked()
    elif data.name == data.p2:
        if data.name.win(data.p1):
            data.screen = "win"
            data.winner = "Player 2"
            data.wins = True
        else:
            data.screen = "play"
            data.win.unClicked()
    else:
            data.screen = "play"
            data.win.unClicked()

def makeTradeButton(data):
    #exit button
    data.exit = Button(775, 160, 25, 25, "red", exit, "X", 18, data)
    data.tradeButton += [data.exit]
    data.sbrick = Button(250, 225, 200, 50, "firebrick4", trade, "Brick", 12, data, "brick")
    data.tradeButton += [data.sbrick]
    data.sore = Button(250, 300, 200, 50, "gray40", trade, "Ore", 12, data, "ore")
    data.tradeButton += [data.sore]
    data.ssheep = Button(250, 375, 200, 50, "SpringGreen4", trade, "Sheep", 12, data, "sheep")
    data.tradeButton += [data.ssheep]
    data.swheat = Button(250, 450, 200, 50, "khaki3", trade, "Wheat", 12, data, "wheat")
    data.tradeButton += [data.swheat]
    data.swood = Button(250, 525, 200, 50, "tan4", trade, "Wood", 12, data, "wood")
    data.tradeButton += [data.swood]
    
    data.bbrick = Button(550, 225, 200, 50, "firebrick4", buy, "Brick", 12, data, "brick")
    data.tradeButton += [data.bbrick]
    data.bore = Button(550, 300, 200, 50, "gray40", buy, "Ore", 12, data, "ore")
    data.tradeButton += [data.bore]
    data.bsheep = Button(550, 375, 200, 50, "SpringGreen4", buy, "Sheep", 12, data, "sheep")
    data.tradeButton += [data.bsheep]
    data.bwheat = Button(550, 450, 200, 50, "khaki3", buy, "Wheat", 12, data, "wheat")
    data.tradeButton += [data.bwheat]
    data.bwood = Button(550, 525, 200, 50, "tan4", buy, "Wood", 12, data, "wood")
    data.tradeButton += [data.bwood]

def buy(data, type):
    if type == "brick":
        data.name.brick += 1
    elif type =="ore":
        data.name.ore += 1
    elif type =="sheep":
        data.name.sheep += 1
    elif type == "wheat":
        data.name.wheat += 1
    elif type == "wood":
        data.name.wood += 1
    data.traded -= 1
    if data.yop == True:
        data.yopCard -= 1
    
def trade(data, type):
    if type == "brick" and data.name.brick >= 4:
        data.name.brick -=4
    elif type =="ore" and data.name.ore >= 4:
        data.name.ore -=4
    elif type =="sheep" and data.name.sheep >= 4:
        data.name.sheep -= 4
    elif type == "wheat" and data.name.wheat >= 4:
        data.name.wheat -=4
    elif type == "wood" and data.name.wood >=4:
        data.name.wood -=4
    data.traded += 1
    

def exit(data):
    if data.traded == 0:
        data.trade = False
        data.trading.unClicked()

def getCloserPoints(data, x, y):
    for keys in data.board.pTN:
        x1, y1 = keys
        if abs(x - x1) <= 20 and abs(y -y1) <= 20:
            return (x1, y1)
    return False

def isValidSettlement(data, x, y):
    # finds the corresponding name to the point
    nNum = data.board.pTN[x, y]
    # uses corresponding name to find all adjacent points
    res = data.board.adjPnts[nNum]
    count = 0
    # looks at the point you grabbed and checks if it has 2 roads around it
    
    for hex in res:
        # checks if any of the adjacent points have things next to them
        if hex in data.board.filledPoints:
            result = data.board.filledPoints[hex]
            for ans in result:
                # if a settlement is adjacent then you can't
                if ans == "p1settlement" or ans == "p2settlement":
                    return False
                elif ans.count("p1road") == 2 or ans.count("p2road") == 2:
                    return False
                elif ans == "%sroad" % data.n1:
                    count += 1
    if nNum not in data.board.filledPoints:
        count = 0
    
    if count >= 1: return True
    
def isValidCity(data, x, y):
    nNum = data.board.pTN[(x, y)]
    if nNum in data.board.filledPoints:
        if "%ssettlement" % data.n1 in data.board.filledPoints[nNum]:
            return True
    return False

# checking if the first point you are putting down is adjacent to a point that has a road or settlement    
def isValidRoad(data, x, y):
    # translation of point into other point
    nNum = data.board.pTN[x, y]
    # all your adjacent bois
    adj = data.board.adjPnts[nNum]
    count = 0
    # iterates through all adjacent points
    for pnts in adj:
        # if adjacent point has stuff on node --> 
        if pnts in data.board.filledPoints:
            items = data.board.filledPoints[pnts]
            for i in items:
                # should be checking that an adjacent point has a road or settlement
                if i == "%ssettlement" % data.n1 or i == "%sroad" % data.n1:
                    count += 1
    if nNum in data.board.filledPoints:
        item = data.board.filledPoints[nNum]
        for i2 in item:
            if i2 == "%ssettlement" % data.n1 or i2 == "%sroad" % data.n1:
                count += 1
    if count >= 1:
        return True
    return False

def mpTrade(data, event):
    x = event.x
    y = event.y
    for b in data.tradeButton:
        if b.click == True: break
        elif x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
        b.unClicked()

def mpSet(event, data):
    x = event.x
    y = event.y 
    buttonClick = False
    for b in data.setButton:
        if b.color == "gray": pass
        elif b.click == True: break
        elif x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
            buttonClick = True
            break
    if buttonClick == False:
        res = getCloserPoints(data, x, y)
        if res != False:
            x, y = res
            rx, ry, n = data.board.pTN[(x, y)]
        # need an else case which will make it so that you cannot do this and undo your move 
        if data.settlement == True:
            if data.screen == "playSet":
                data.settlement = False
                rx , ry, n = data.board.pTN[(x, y)]
                if (rx, ry, n) in data.board.filledPoints:
                    if not isValidSettlement(data, x, y):
                        data.settlement = True
                    else:
                        data.settlements.append(Settlement(x, y, data.name.color))
                        # gives a list of tuples with adjoining 
                        possHex = data.board.hexNum[(x, y)]
                        for hexes in possHex:
                            type, num = data.board.tileNum[hexes]
                            soln = [type] + data.name.resources.get(num, [])
                            data.name.resources[num] = soln
                        fill = ["%ssettlement" % data.n1] + data.board.filledPoints.get((rx, ry, n), [])
                        data.board.filledPoints[(rx, ry, n)] = fill
                        data.name.scount += 1
                        data.name.points += 1
                        data.setsettlement.unClicked()
                else:
                    data.settlements.append(Settlement(x, y, data.name.color))
                    # gives a list of tuples with adjoining 
                    possHex = data.board.hexNum[(x, y)]
                    for hexes in possHex:
                        type, num = data.board.tileNum[hexes]
                        soln = [type] + data.name.resources.get(num, [])
                        data.name.resources[num] = soln
                    fill = ["%ssettlement" % data.n1] + data.board.filledPoints.get((rx, ry, n), [])
                    data.board.filledPoints[(rx, ry, n)] = fill
                    data.name.scount += 1
                    data.name.points += 1
                    data.setsettlement.unClicked()
                
        elif data.road == True:
            if data.clicked == 0:
                data.x1 = event.x
                data.y1 = event.y
                res = getCloserPoints(data, data.x1, data.y1)
                counter = 0
                if res != False:
                    data.x1, data.y1 = res
                    x3, y3, n3 = data.board.pTN[(data.x1, data.y1)]
                    adj2 = data.board.adjPnts[(x3, y3, n3)]
                    if not isValidRoad(data, data.x1, data.y1): data.clicked = -1
    
            # ensures that you are making the second point only on one side --> not going crazy
            # need to make sure that when you are placing these roads that they are adjacent
            if data.clicked == 1: 
                if not isValidRoad(data, x, y):
                    data.clicked = 0
                else:
                    x3, y3, n3 = data.board.pTN[(data.x1, data.y1)]
                    adj2 = data.board.adjPnts[(x3, y3, n3)]
                    if (rx, ry, n) not in adj2:
                        data.clicked = 0
                    elif (x3, y3, n3) not in data.board.filledPoints and (rx, ry, n) not in data.board.filledPoints:
                        data.clicked = 0
                            
            data.clicked += 1
                            
            if data.clicked > 1:
                data.roads.append(Road(data.x1, data.y1, x, y, data.name.color))
                x1, y1, n1 = data.board.pTN[(x, y)]
                fill = ["%sroad" % data.n1] + data.board.filledPoints.get((x1, y1, n1), [])
                data.board.filledPoints[(x1, y1, n1)] = fill
                x2, y2, n2 = data.board.pTN[(data.x1, data.y1)]
                fill2 = ["%sroad" % data.n1] + data.board.filledPoints.get((x2, y2, n2), [])
                data.board.filledPoints[(x2, y2, n2)] = fill2
                data.x1 = 0
                data.y1 = 0
                data.clicked = 0
                data.name.rcount += 1
                data.road = False
                data.name.drawRoad()
                data.setroad.unClicked()
                
        if data.name == data.first and data.name.isFirst:
            if data.name.scount == 1 and data.name.rcount == 1:
                data.name.isFirst = False
                endTurnNow(data)
        elif data.name.scount == 2 and data.name.rcount == 2 and data.name.isFirst:
            data.name.isFirst = False
            endTurnNow(data)
        elif data.name.scount == 2 and data.name.rcount == 2 and not data.name.isFirst:
            data.screen = "play"
            givePlayersCards(data)

def mpStart(event, data):
    if data.i == True:
        mpinstruct(event, data)
    x = event.x
    y = event.y
    for b in data.startButton:
        if x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
            return
        b.unClicked()
            
def mpinstruct(event, data):
    x = event.x
    y = event.y
    if x >= data.Instruction.x and x <= data.Instruction.x + data.Instruction.width and y >= data.Instruction.y and y <= data.Instruction.y + data.Instruction.height:
        data.Instruction.isClicked()

def mplc(event, data):
    x = event.x
    y = event.y
    if x >= data.hCard.x and x <= data.hCard.x + data.hCard.width and y >= data.hCard.y and y <= data.hCard.y + data.hCard.height:
        data.hCard.isClicked()
    data.hCard.unClicked() 

def mpdvc(event, data):
    if data.yop == True:
        mpyop(event, data)
        return
    elif data.mon == True:
        mpmon(event, data)
        return
    elif data.learnCard == True:
        mplc(event, data)
        return
    x = event.x
    y = event.y
    for b in data.dvcButton:
        if b.click == True: break
        elif x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
        b.unClicked() 
        
def mpmon(event, data):
    x = event.x
    y = event.y
    for b in data.monCards:
        if b.click == True: break
        elif x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
        b.unClicked()
        data.seedvc.unClicked() 
        data.mon = False
        data.viewdvc = False
        
def mpyop(event, data):
    x = event.x
    y = event.y
    for b in data.yopCards:
        if b.click == True: break
        elif x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
        b.unClicked() 
    if data.yopCard == 0:
        data.yop = False
        data.viewdvc = False
        data.seedvc.unClicked()
        data.yopCards = 2
    
def mousePressed(event, data):
    if data.trade == True:
        mpTrade(data, event)
        return
    elif data.screen == "playSet":
        mpSet(event, data)
        return
    elif data.viewdvc == True:
        mpdvc(event, data)
        return
    elif data.screen == "start":
        mpStart(event, data)
        return
    x = event.x
    y = event.y
    for b in data.playButton:
        if b.click == True: break
        elif x >= b.x and x <= b.x + b.width and y >= b.y and y <= b.y + b.height:
            b.isClicked()
            if b == data.prollDie or b == data.endTurn or b == data.pdvc or b == data.win:
                b.unClicked()
            return
        # b.unClicked()
        
    # call a function that will do this?
    res = getCloserPoints(data, x, y)
    if res != False:
        x, y = res
        rx, ry, n = data.board.pTN[(x, y)]
    # need an else case which will make it so that you cannot do this and undo your move 
    if data.settlement == True:
        if isValidSettlement(data, x, y) and data.screen == "play":
            data.name.drawSettlement()
            data.settlement = False
            data.settlements.append(Settlement(x, y, data.name.color))
            # gives a list of tuples with adjoining 
            possHex = data.board.hexNum[(x, y)]
            for hexes in possHex:
                type, num = data.board.tileNum[hexes]
                soln = [type] + data.name.resources.get(num, [])
                data.name.resources[num] = soln
            fill = ["%ssettlement" % data.n1] + data.board.filledPoints.get((rx, ry, n), [])
            data.board.filledPoints[(rx, ry, n)] = fill
            data.psettlement.unClicked()
       # need to make sure that if you are placing next to something then stop!
            
    elif data.city == True:
        if isValidCity(data, x, y):
            data.city = False
            data.name.drawCity()
            data.cities.append(City(x, y, data.name.color))
            data.settlements.remove(Settlement(x, y, data.name.color))
            possHex = data.board.hexNum[(x, y)]
            for hexes in possHex:
                type, num = data.board.tileNum[hexes]
                soln = [type] + data.name.resources.get(num, [])
                data.name.resources[num] = soln
            fill = ["%scity" % data.n1] + data.board.filledPoints.get((rx, ry, n), [])
            data.board.filledPoints[(rx, ry, n)] = fill
            data.pcity.unClicked()
    elif data.road == True:
        if data.clicked == 0:
            data.x1 = event.x
            data.y1 = event.y
            res = getCloserPoints(data, data.x1, data.y1)
            counter = 0
            if res != False:
                data.x1, data.y1 = res
                x3, y3, n3 = data.board.pTN[(data.x1, data.y1)]
                adj2 = data.board.adjPnts[(x3, y3, n3)]
                if not isValidRoad(data, data.x1, data.y1): data.clicked = -1

        # ensures that you are making the second point only on one side --> not going crazy
        # need to make sure that when you are placing these roads that they are adjacent
        if data.clicked == 1: 
            if not isValidRoad(data, x, y):
                data.clicked = 0
            else:
                x3, y3, n3 = data.board.pTN[(data.x1, data.y1)]
                adj2 = data.board.adjPnts[(x3, y3, n3)]
                if (rx, ry, n) not in adj2:
                    data.clicked = 0
                elif (x3, y3, n3) not in data.board.filledPoints and (rx, ry, n) not in data.board.filledPoints:
                    data.clicked = 0
                        
        data.clicked += 1
                        
        if data.clicked > 1:
            data.roads.append(Road(data.x1, data.y1, x, y, data.name.color))
            x1, y1, n1 = data.board.pTN[(x, y)]
            fill = ["%sroad" % data.n1] + data.board.filledPoints.get((x1, y1, n1), [])
            data.board.filledPoints[(x1, y1, n1)] = fill
            x2, y2, n2 = data.board.pTN[(data.x1, data.y1)]
            fill2 = ["%sroad" % data.n1] + data.board.filledPoints.get((x2, y2, n2), [])
            data.board.filledPoints[(x2, y2, n2)] = fill2
            data.x1 = 0
            data.y1 = 0
            data.clicked = 0
            data.name.rcount += 1
            data.road = False
            data.proad.unClicked()
            data.name.drawRoad()
            if data.rb == True:
                data.countRoad -=1
                if data.countRoad == 0: 
                    data.road = False
                    data.rb = False
                else: data.road = True
        
    if data.screen == "playSet":
        if data.name == data.first and data.name.isFirst:
            if data.name.scount == 1 and data.name.rcount == 2:
                data.name.isFirst = False
                endTurnNow(data)
        elif data.name.scount == 2 and data.name.rcount == 4 and data.name.isFirst:
            data.name.isFirst = False
            endTurnNow(data)
        elif data.name.scount == 2 and data.name.rcount == 4 and not data.name.isFirst:
            data.screen = "play"
            givePlayersCards(data)

        
def keyPressed(event, data):
    if event.keysym == "n":
        init(data)

def givePlayersCards(data):
    for nums in data.p1.resources:
        r = data.p1.resources[nums]
        data.p1.brick += r.count("brick")
        data.p1.wood += r.count("wood")
        data.p1.sheep += r.count("sheep")
        data.p1.wheat += r.count("wheat")
        data.p1.ore += r.count("ore")
        
    for num in data.p2.resources:            
        r2 = data.p2.resources[num]
        data.p2.brick += r2.count("brick")
        data.p2.wood += r2.count("wood")
        data.p2.sheep += r2.count("sheep")
        data.p2.wheat += r2.count("wheat")
        data.p2.ore += r2.count("ore")

def setSettlement(data):
    data.settlement = True

def setRoad(data):
    data.road = True

def buildSettlement(data):
    if data.roll == True:
        s = data.name.buySettlement()
        if s != None: data.settlement = True
    else:
        data.settlement = False
        data.psettlement.unClicked()
    
def buildRoad(data):
    if data.roll == True:
        r = data.name.buyRoad()
        if r != None: 
            data.road = True
    else:
        print("YIKES")
        data.road = False
        data.proad.unClicked()
        print("YO")
    
def buildCity(data):
    if data.roll == True:
        c = data.name.buyCity()
        if c!= None: data.city = True
    else: 
        data.pcity.unClicked()
        data.city = False
    
def buyDVC(data):
    if data.roll == True:
        data.name.buyDVC()
        card = data.board.buyDevCard()
        if card == "VP":
            data.name.points += 1
        data.name.cards += [card]
        

def drawStart(canvas, data):
    txt = "Welcome to Settlers of Catan!"
    canvas.create_text(data.width / 2, 50, text = txt, anchor = "c", font = ("Arial", 30))
    for b in data.startButton:
        b.draw(canvas)

def drawInstructions(canvas, data):
    canvas.create_rectangle(data.width / 10, data.height / 10, data.width * 9 / 10, data.height * 9 / 10, fill = "LightBlue4")
    data.Instruction.draw(canvas)
    canvas.create_text(data.width / 2, 150, text = "Instructions", font = ("Arial", 20))
    canvas.create_text(data.width / 2, 200, text = "To see full instructions visit:", font = ("Arial", 18))
    canvas.create_text(data.width / 2, 250, text = "bit.ly/catanRules", font = ("Arial", 30) )
    canvas.create_text(150, 300, text = "The Summary:", font = ("Arial", 25), anchor = "nw")
    canvas.create_text(200, 350, text = "Roads", font = ("Arial", 15, "bold"), anchor = "nw")
    canvas.create_text(225, 375, text = "Click on 2 adjacent points to build a road! \n Your road must connect to either one of your roads or one of your settlements!", font = ("Arial", 12), anchor = "nw")
    canvas.create_text(200, 415, text = "Settlements", font = ("Arial", 15, "bold"), anchor = "nw")
    canvas.create_text(225, 435, text = "Click on 1 point to build a settlement \n Your settlement cannot be adjacent to any other settlements!", font = ("Arial", 12), anchor = "nw")
    canvas.create_text(200, 475, text = "Cities", font = ("Arial", 15, "bold"), anchor = "nw")
    canvas.create_text(225, 495, text = "You get one extra victory point and\nyou get one extra resource for the hexes that the city is on.\nClick on a settlement to build a city!", font = ("Arial", 12), anchor = "nw")
    canvas.create_text(200, 545, text = "Development Cards", font = ("Arial", 15, "bold"), anchor = "nw")
    canvas.create_text(225, 565, text = "Play development cards to advance your standings!", font = ("Arial", 12), anchor = "nw")
    
 
# access the name and then add if statements to change number of resources of each thing
def rollDie(data):
    if data.roll == False and data.screen == "play":
        data.die1.rollDie()
        data.die2.rollDie()
        data.totalRoll = data.die1.num + data.die2.num
        if data.totalRoll in data.p1.resources:       
            r = data.p1.resources[data.totalRoll]
            data.p1.brick += r.count("brick")
            data.p1.wood += r.count("wood")
            data.p1.sheep += r.count("sheep")
            data.p1.wheat += r.count("wheat")
            data.p1.ore += r.count("ore")
        if data.totalRoll in data.p2.resources:       
            r2 = data.p2.resources[data.totalRoll]
            data.p2.brick += r2.count("brick")
            data.p2.wood += r2.count("wood")
            data.p2.sheep += r2.count("sheep")
            data.p2.wheat += r2.count("wheat")
            data.p2.ore += r2.count("ore")
        data.roll = True
    data.prollDie.unClicked()

def endTurnNow(data):
    if data.roll == True:
        data.player1 = not data.player1
        data.roll = False
        data.clicked = 0
        if data.name == data.p1: 
            data.name = data.p2
            data.n1 = "p2"
        else: 
            data.name = data.p1
            data.n1 = "p1"
    elif not data.name.isFirst:
        data.player1 = not data.player1
        data.roll = False
        if data.name == data.p1: 
            data.name = data.p2
            data.n1 = "p2"
        else: 
            data.name = data.p1
            data.n1 = "p1"
    data.endTurn.unClicked()

    
def drawSet(canvas, data):
    if data.name == data.p1:
        name = "Player 1"
    else: name = "Player 2"
    canvas.create_text(875, 100, text = name, font = ("Arial", 18))
    canvas.create_text(875, 350, text = "brick  x%d" % data.name.brick)
    canvas.create_text(875, 370, text = "ore x%d" % data.name.ore)
    canvas.create_text(875, 390, text = "wheat x%d" % data.name.wheat)
    canvas.create_text(875, 410, text = "sheep x%0d" % data.name.sheep)
    canvas.create_text(875, 430, text = "wood x%d" % data.name.wood)
    canvas.create_text(875, 450, text = "knight cards played x%d" % data.name.knightsPlayed)
    canvas.create_text(875, 470, text = "%d"% data.name.points)
    for b in data.setButton:
        b.draw(canvas)


def drawPlay(canvas, data):
    data.board.drawBoard(canvas)
    for r in data.roads:
        r.draw(canvas)
    for s in data.settlements:
        s.draw(canvas)
    for c in data.cities:
        c.draw(canvas)
    data.robber.draw(canvas)
    canvas.create_rectangle(825, 225, 875, 275, fill = "red")
    canvas.create_rectangle(900, 225, 950, 275, fill = "red")
    canvas.create_text(850, 250, text = data.die1.num, font = ("Arial", 15, "bold"), fill = "white")
    canvas.create_text(925, 250, text = data.die2.num, font = ("Arial", 15, "bold"), fill = "white")
 
def drawPlay2(canvas, data):
    if data.name == data.p1:
        name = "Player 1"
    else: name = "Player 2"
    canvas.create_text(875, 100, text = name, font = ("Arial", 18))
    canvas.create_text(875, 350, text = "brick  x%d" % data.name.brick)
    canvas.create_text(875, 370, text = "ore x%d" % data.name.ore)
    canvas.create_text(875, 390, text = "wheat x%d" % data.name.wheat)
    canvas.create_text(875, 410, text = "sheep x%0d" % data.name.sheep)
    canvas.create_text(875, 430, text = "wood x%d" % data.name.wood)
    canvas.create_text(875, 450, text = "knight cards played x%d" % data.name.knightsPlayed)
    canvas.create_text(875, 470, text = "%d"% data.name.points)
    for b in data.playButton:
        b.draw(canvas)
    if data.rb == True:
        canvas.create_text(250, 100, text = "You played a road building Card!", font = ("Arial", 12))
        canvas.create_text(250, 150, text = "Roads remaining: %d" % data.countRoad, font = ("Arial", 12))
    
def drawdvc(canvas, data):
    canvas.create_rectangle(data.width / 5, data.height / 5, data.width * 4 / 5, data.height * 4 / 5, fill = "peach puff")
    canvas.create_text(data.width / 2, 200, text = "Development Cards", font = ("Arial", 20))
    canvas.create_text(350, 250, text = "%d" % data.name.cards.count("knight"), font = ("Arial", 30))
    canvas.create_text(650, 250, text = "%d" % data.name.cards.count("YOP"), font = ("Arial", 30))
    canvas.create_text(350, 450, text = "%d" % data.name.cards.count("RB"), font = ("Arial", 30))
    canvas.create_text(650, 450, text = "%d" % data.name.cards.count("mon"), font = ("Arial", 30))
    canvas.create_text(500, 600, text = "Victory Points: %d" % data.name.cards.count("VP"), font = ("Arial", 14))
    for b in data.dvcButton:
        b.draw(canvas)
    if data.yop == True:
        drawyop(canvas, data)
    elif data.mon == True:
        drawmon(canvas, data)
    elif data.learnCard == True:
        drawLearn(canvas, data)
        
def drawLearn(canvas, data):
    canvas.create_rectangle(data.width * 3 / 10, data.height / 5, data.width * 7 / 10, data.height * 4 / 5, fill = "gray93" )
    data.hCard.draw(canvas)
    canvas.create_text(data.width / 2, 200, text = "What does each card mean?", font = ("Arial", 14))
    canvas.create_text(325, 250, text = "Knight: Randomly take one card from your opponent", font = ("Arial", 11), anchor = "nw")
    canvas.create_text(325, 300, text = "Year of Plenty: Pick 2 resources from the bank", font = ("Arial", 11), anchor = "nw")
    canvas.create_text(325, 350, text = "Monopoly: Take all of one type of resource \nfrom your opponent", font = ("Arial", 11), anchor = "nw")
    canvas.create_text(325, 400, text = "Road Building: Build 2 roads on behalf of the bank", font = ("Arial", 11), anchor = "nw")
    canvas.create_text(325, 450, text = "Victory Point: Add one point to your victory point", font = ("Arial", 11), anchor = "nw")
        
def drawmon(canvas, data):
    canvas.create_rectangle(data.width * 3 / 10, data.height / 5, data.width * 7 / 10, data.height * 4 / 5, fill = "gray" )
    for b in data.monCards:
        b.draw(canvas)
    canvas.create_text(data.width / 2, 200, text = "Pick 1 card to monopolize!", font = ("Arial", 12))

    
def drawyop(canvas, data):
    canvas.create_rectangle(data.width * 3 / 10, data.height / 5, data.width * 7 / 10, data.height * 4 / 5, fill = "gray" )
    for b in data.yopCards:
        b.draw(canvas)
    canvas.create_text(data.width / 2, 200, text = "Pick 2 cards you would like from the bank!", font = ("Arial", 12))
    canvas.create_text(data.width / 2, 600, text = "Remaining cards: %d" % data.yopCard)

def drawInfo(canvas, data):
    if data.screen == "playSet":
        drawSet(canvas, data)
        drawPlay(canvas, data)
    elif data.screen == "play":
        drawPlay2(canvas, data)
        drawPlay(canvas, data)
    if data.trade == True:
        drawTrade(canvas, data)
        for b in data.tradeButton:
            b.draw(canvas)
    elif data.viewdvc == True:
        drawdvc(canvas, data)
        
def drawTrade(canvas, data):
    canvas.create_rectangle(data.width / 5, data.height / 5, data.width * 4 / 5, data.height * 4 / 5, fill = "peach puff")
    canvas.create_text(350, 200, text = "Pick what you want to trade the bank")
    canvas.create_text(650, 200, text = "Pick what you want to receive from the bank")
    canvas.create_text(600, 600, text = "Remaining Trades: %d" % data.traded)
    
def redrawAll(canvas, data):
    canvas.create_rectangle(-5, -5, data.width + 5 , data.height + 5, fill = "Light Blue1")
    if data.i == True:
        drawInstructions(canvas, data)
    elif data.screen == "start":
        drawStart(canvas, data)
    elif data.screen == "playSet" or data.screen == "play":
        drawInfo(canvas, data)
    if data.wins == True:
        drawWin(canvas, data)
        
def drawWin(canvas, data):
    canvas.create_rectangle(-5, -5, data.width + 5, data.height + 5, fill = "LightBlue1")
    canvas.create_text(data.width / 2, data.height / 2, text = "%s wins!" % data.winner, font = ("Arial", 30, "bold"))

    
    
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # data.canvas = canvas
    init(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 800)