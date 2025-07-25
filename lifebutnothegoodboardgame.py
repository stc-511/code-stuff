import random
import os
import time

def makeaboardforlifbutnotthegoodboardgameifier():
    thebetterlist = []
    for i in range(30):
        theworselist = []
        for o in range(30):
            randum = random.random()
            if randum >= 0.1:
                theworselist.append(False)
            else:
                theworselist.append(True)
        thebetterlist.append(theworselist)
    return thebetterlist
def printtheboardforlifebutnotthegoodboardgameifierifier(listymclistface):
    time.sleep(1)
    os.system('cls||clear')
    for i in range(len(listymclistface)):
        for o in range(len(listymclistface)):
            if listymclistface[i][o]:
                print("🟨", end = "")
            else:
                print("⬛", end = "")
        print()
def areyouanantisocialcubeatoosocialcubeoralivingcubechecker(x, y, board):
    neighburs = 0
    for i in range(-1,2):
        for o in range(-1,2):
            if x+o >= len(board) or y+i >= len(board) or x+o < 0 or y+i < 0 or (i == 0 and o == 0):
                continue
            if board[x + o][y + i]:
                neighburs += 1
    return neighburs
def returnthenextgenerationofprinttheboardforlifebutnotthegoodboardgameifierifierifier(board):
    bebyarry = []
    for i in range(len(board)):
        listy = []
        for o in range(len(board)):
            neighbors = areyouanantisocialcubeatoosocialcubeoralivingcubechecker(i,o,board)
            if board[i][o]:
                if neighbors < 2 or neighbors > 3:
                    listy.append(False)
                else:
                    listy.append(True)
            else:
                if neighbors == 3:
                    listy.append(True)
                else:
                    listy.append(False)
        bebyarry.append(listy)
    return bebyarry

baord = makeaboardforlifbutnotthegoodboardgameifier()
printtheboardforlifebutnotthegoodboardgameifierifier(baord)
while True:
    baord = returnthenextgenerationofprinttheboardforlifebutnotthegoodboardgameifierifierifier(baord)
    printtheboardforlifebutnotthegoodboardgameifierifier(baord)