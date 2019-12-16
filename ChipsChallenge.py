import pygame, sys, random, time
from pygame.locals import *
from pygame.font import *

with open('CCLvl1.txt') as lvlOne:
    linesOne = [line.split() for line in lvlOne]

with open('CCLvl2.txt') as lvlTwo:
    linesTwo = [line.split() for line in lvlTwo]

BOARDWIDTH = 9
BOARDHEIGHT = 9
TILESIZE = 90
WINDOWWIDTH = 810
WINDOWHEIGHT = 900
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
DARKGRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SEABLUE = (0, 105, 148)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
ICEBLUE = (165, 242, 243)
DIRT = (124, 94, 66)
DIMGRAY = (64, 64, 64)
ORANGE = (255, 165, 0)
CHARCOAL = (21, 27, 31)
DARKORANGE = (255, 140, 0)

TILECOLOR = LIGHTGRAY
TEXTCOLOR = BLACK
BORDERCOLOR = DARKGRAY
BASICFONTSIZE = 20

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Chip's Challenge")
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    MAPHEIGHT = len(linesOne)
    MAPWIDTH = len(linesOne[0])

    nxtLvl = False
    levelTwo = False
    levelTwoX = 3
    levelTwoY = 9
    mainBoard = []
    for x in range(MAPWIDTH):
        mainBoard.append(linesOne[x])

    mapY = (int)(MAPHEIGHT/2 - 1)
    mapX = (int)(MAPWIDTH/2)
    inventory = []
    for x in range(0, 9):
        inventory.append("E")

    dead = False
    time = 0
    finishTime = 0
    initialTime = 0
    completed = False
    running = True
    win = False

    spriteOneX = 26
    spriteOneY = 7
    spriteTwoX = 28
    spriteTwoY = 11
    spriteThreeX = 2
    spriteThreeY = 7
    spriteFourX = 4
    spriteFourY = 11
    spriteFiveX = 14
    spriteFiveY = 7
    spriteSixX = 16
    spriteSixY = 11
    spriteDirection = "Down"

    while True:
        if nxtLvl:
            MAPHEIGHT = len(linesTwo)
            MAPWIDTH = len(linesTwo[0])
            for x in range(MAPHEIGHT):
                mainBoard[x] = linesTwo[x]
            mapY = levelTwoY
            mapX = levelTwoX
            for i in range(0, 9):
                inventory[i] = "E"
            nxtLvl = False
            levelTwo = True
            initialTime = pygame.time.get_ticks()
            completed = False
            running = True
        hint = False
        if mainBoard[mapY][mapX] == "s":
            hint = True
        drawBoard(mainBoard, mapX, mapY, inventory, dead, MAPWIDTH, MAPHEIGHT, levelTwo, time, completed, finishTime, hint, win, spriteOneX, spriteOneY, spriteTwoX, spriteTwoY, spriteThreeX, spriteThreeY, spriteFourX, spriteFourY, spriteFiveX, spriteFiveY, spriteSixX, spriteSixY)

        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key in (K_LEFT, K_a) and not dead and not completed:
                    if not mainBoard[mapY][mapX - 1] == "W" and not mainBoard[mapY][mapX - 1] == "R" and not mainBoard[mapY][mapX - 1] == "O" and not mainBoard[mapY][mapX - 1] == "B" and not mainBoard[mapY][mapX - 1] == "P" and not mainBoard[mapY][mapX - 1] == "G" and not mainBoard[mapY][mapX - 1] == "M":
                        mapX = mapX - 1
                    elif mainBoard[mapY][mapX - 1] == "R" or mainBoard[mapY][mapX - 1] == "O" or mainBoard[mapY][mapX - 1] == "B" or mainBoard[mapY][mapX - 1] == "P" or mainBoard[mapY][mapX - 1] == "G":
                        go = True
                        i = 0
                        s = mainBoard[mapY][mapX - 1].lower()
                        while go:
                            if inventory[i] == s:
                                inventory[i] = "E"
                                mainBoard[mapY][mapX - 1] = "N"
                                go = False
                            if i == 8:
                                go = False
                            i += 1
                    elif mainBoard[mapY][mapX - 1] == "M" and mainBoard[mapY][mapX - 2] == "N":
                        bulldozer = False
                        for item in inventory:
                            if item == "C":
                                bulldozer = True
                        if bulldozer:
                            mainBoard[mapY][mapX - 1] = "N"
                            mainBoard[mapY][mapX - 2] = "M"
                            mapX = mapX - 1
                    elif mainBoard[mapY][mapX] == "D" and mainBoard[mapY][mapX - 1] == "W":
                        shovel = False
                        for item in inventory:
                            if item == "h":
                                shovel = True
                        if shovel:
                            mapX = mapX - 2
                if event.key in (K_RIGHT, K_d) and not dead and not completed:
                    if not mainBoard[mapY][mapX + 1] == "W" and not mainBoard[mapY][mapX + 1] == "R" and not mainBoard[mapY][mapX + 1] == "O" and not mainBoard[mapY][mapX + 1] == "B" and not mainBoard[mapY][mapX + 1] == "P" and not mainBoard[mapY][mapX + 1] == "G" and not mainBoard[mapY][mapX + 1] == "M":
                        mapX = mapX + 1
                    elif mainBoard[mapY][mapX + 1] == "R" or mainBoard[mapY][mapX + 1] == "O" or mainBoard[mapY][mapX + 1] == "B" or mainBoard[mapY][mapX + 1] == "P" or mainBoard[mapY][mapX + 1] == "G":
                        go = True
                        i = 0
                        s = mainBoard[mapY][mapX + 1].lower()
                        while go:
                            if inventory[i] == s:
                                inventory[i] = "E"
                                mainBoard[mapY][mapX + 1] = "N"
                                go = False
                            if i == 8:
                                go = False
                            i += 1
                    elif mainBoard[mapY][mapX + 1] == "M" and mainBoard[mapY][mapX + 2] == "N":
                        bulldozer = False
                        for item in inventory:
                            if item == "C":
                                bulldozer = True
                        if bulldozer:
                            mainBoard[mapY][mapX + 1] = "N"
                            mainBoard[mapY][mapX + 2] = "M"
                            mapX = mapX + 1
                    elif mainBoard[mapY][mapX] == "D" and mainBoard[mapY][mapX + 1] == "W":
                        shovel = False
                        for item in inventory:
                            if item == "h":
                                shovel = True
                        if shovel:
                            mapX = mapX + 2
                if event.key in (K_UP, K_w) and not dead and not completed:
                    if not mainBoard[mapY - 1][mapX] == "W" and not mainBoard[mapY - 1][mapX] == "R" and not mainBoard[mapY - 1][mapX] == "O" and not mainBoard[mapY - 1][mapX] == "B" and not mainBoard[mapY - 1][mapX] == "P" and not mainBoard[mapY - 1][mapX] == "G" and not mainBoard[mapY - 1][mapX] == "M":
                        mapY = mapY - 1
                    elif mainBoard[mapY - 1][mapX] == "R" or mainBoard[mapY - 1][mapX] == "O" or mainBoard[mapY - 1][mapX] == "B" or mainBoard[mapY - 1][mapX] == "P" or mainBoard[mapY - 1][mapX] == "G":
                        go = True
                        i = 0
                        s = mainBoard[mapY - 1][mapX].lower()
                        while go:
                            if inventory[i] == s:
                                inventory[i] = "E"
                                mainBoard[mapY - 1][mapX] = "N"
                                go = False
                            if i == 8:
                                go = False
                            i += 1
                    elif mainBoard[mapY - 1][mapX] == "M" and mainBoard[mapY - 2][mapX] == "N":
                        bulldozer = False
                        for item in inventory:
                            if item == "C":
                                bulldozer = True
                        if bulldozer:
                            mainBoard[mapY - 1][mapX] = "N"
                            mainBoard[mapY - 2][mapX] = "M"
                            mapY = mapY - 1
                if event.key in (K_DOWN, K_s) and not dead and not completed:
                    if not mainBoard[mapY + 1][mapX] == "W" and not mainBoard[mapY + 1][mapX] == "R" and not mainBoard[mapY + 1][mapX] == "O" and not mainBoard[mapY + 1][mapX] == "B" and not mainBoard[mapY + 1][mapX] == "P" and not mainBoard[mapY + 1][mapX] == "G" and not mainBoard[mapY + 1][mapX] == "M":
                        mapY = mapY + 1
                    elif mainBoard[mapY + 1][mapX] == "R" or mainBoard[mapY + 1][mapX] == "O" or mainBoard[mapY + 1][mapX] == "B" or mainBoard[mapY + 1][mapX] == "P" or mainBoard[mapY + 1][mapX] == "G":
                        go = True
                        i = 0
                        s = mainBoard[mapY + 1][mapX].lower()
                        while go:
                            if inventory[i] == s:
                                inventory[i] = "E"
                                mainBoard[mapY + 1][mapX] = "N"
                                go = False
                            if i == 8:
                                go = False
                            i += 1
                    elif mainBoard[mapY + 1][mapX] == "M" and (mainBoard[mapY + 2][mapX] == "N" or mainBoard[mapY + 2][mapX] == "H"):
                        bulldozer = False
                        for item in inventory:
                            if item == "C":
                                bulldozer = True
                        if bulldozer:
                            mainBoard[mapY + 1][mapX] = "N"
                            if mainBoard[mapY + 2][mapX] == "H":
                                mainBoard[mapY + 2][mapX] = "N"
                            else:
                                mainBoard[mapY + 2][mapX] = "M"
                            mapY = mapY + 1
                if event.key in (K_SPACE, K_x) and dead:
                    if levelTwo == False:
                        with open('CCLvl1.txt') as lvlOne:
                            linesThree = [line.split() for line in lvlOne]
                        for x in range(MAPWIDTH):
                            mainBoard[x] = linesThree[x]
                        mapY = (int)(MAPHEIGHT / 2 - 1)
                        mapX = (int)(MAPWIDTH / 2)
                    elif levelTwo:
                        with open('CCLvl2.txt') as lvlTwo:
                            linesFour = [line.split() for line in lvlTwo]
                        for x in range(MAPHEIGHT):
                            mainBoard[x] = linesFour[x]
                        mapY = levelTwoY
                        mapX = levelTwoX
                    for x in range(0, 9):
                        inventory[x] = "E"
                    dead = False
                    initialTime = pygame.time.get_ticks()
                if event.key in (K_SPACE, K_x) and completed:
                    nxtLvl = True
                    initialTime = pygame.time.get_ticks()
                if event.key in (K_SPACE, K_x) and win:
                    terminate()

        if checkDie(mainBoard[mapY][mapX], mapX, mapY, inventory, spriteOneX, spriteOneY, spriteTwoX, spriteTwoY, spriteThreeX, spriteThreeY, spriteFourX, spriteFourY, spriteFiveX, spriteFiveY, spriteSixX, spriteSixY, levelTwo):
            dead = True

        if not mainBoard[mapY][mapX] == "N":
            if mainBoard[mapY][mapX] == "r" or mainBoard[mapY][mapX] == "o" or mainBoard[mapY][mapX] == "b" or mainBoard[mapY][mapX] == "p" or mainBoard[mapY][mapX] == "g" or mainBoard[mapY][mapX] == "C" or mainBoard[mapY][mapX] == "h" or mainBoard[mapY][mapX] == "i" or mainBoard[mapY][mapX] == "f" or mainBoard[mapY][mapX] == "S":
                go = True
                i = 0
                while go:
                    if inventory[i] == "E":
                        inventory[i] = mainBoard[mapY][mapX]
                        go = False
                    if i == 8:
                        go = False
                    i += 1
                mainBoard[mapY][mapX] = "N"
            if mainBoard[mapY][mapX] == "w":
                completed = True
                if running:
                    finishTime = int((pygame.time.get_ticks() - initialTime) / 1000)
                running = False
            if mainBoard[mapY][mapX] == "U":
                win = True
                if running:
                    finishTime = int((pygame.time.get_ticks() - initialTime) / 1000)
                running = False

        if time % 2 == 0:
            if spriteDirection == "Down" and spriteOneY < 11:
                spriteOneY += 1
                spriteTwoY -= 1
                spriteThreeY += 1
                spriteFourY -= 1
                spriteFiveY += 1
                spriteSixY -= 1
            elif spriteDirection == "Down":
                spriteDirection = "Up"
                spriteOneY -= 1
                spriteTwoY += 1
                spriteThreeY -= 1
                spriteFourY += 1
                spriteFiveY -= 1
                spriteSixY += 1
            elif spriteDirection == "Up" and spriteOneY > 7:
                spriteOneY -= 1
                spriteTwoY += 1
                spriteThreeY -= 1
                spriteFourY += 1
                spriteFiveY -= 1
                spriteSixY += 1
            elif spriteDirection == "Up":
                spriteDirection = "Down"
                spriteOneY += 1
                spriteTwoY -= 1
                spriteThreeY += 1
                spriteFourY -= 1
                spriteFiveY += 1
                spriteSixY -= 1

        time = int((pygame.time.get_ticks() - initialTime) / 1000)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def checkDie(block, x, y, invent, oneX, oneY, twoX, twoY, threeX, threeY, fourX, fourY, fiveX, fiveY, sixX, sixY, level):
    water = False
    fire = False
    ice = False
    for item in invent:
        if item == "S":
            water = True
        if item == "f":
            fire = True
        if item == "i":
            ice = True
    if block == "H" and not water:
        return True
    if block == "F" and not fire:
        return True
    if block == "I" and not ice:
        return True
    if x == oneX and y == oneY and level:
        return True
    if x == twoX and y == twoY and level:
        return True
    if x == threeX and y == threeY and level:
        return True
    if x == fourX and y == fourY and level:
        return True
    if x == fiveX and y == fiveY and level:
        return True
    if x == sixX and y == sixY and level:
        return True
    return False

def terminate():
    pygame.quit()
    sys.exit()

def drawBoard(board, x, y, inventory, dead, MAPWIDTH, MAPHEIGHT, lvl, time, completed, finishTime, hint, win, oneX, oneY, twoX, twoY, threeX, threeY, fourX, fourY, fiveX, fiveY, sixX, sixY):
    if lvl:
        MAPHEIGHT += 1
        board[oneY][oneX] = "Sprite"
        board[twoY][twoX] = "Sprite"
        board[threeY][threeX] = "Sprite"
        board[fourY][fourX] = "Sprite"
        board[fiveY][fiveX] = "Sprite"
        board[sixY][sixX] = "Sprite"
    DISPLAYSURF.fill(BLACK)
    if x <= 3 and y <= 3:
        xStarting = (int)(4 - x)
        yStarting = (int)(4 - y)
        for x in range(0, 9 - xStarting):
            for y in range(0, 9 - yStarting):
                drawTile(board[y][x], y + yStarting, x + xStarting)
    elif (MAPWIDTH - x) <= 5 and y <= 3:
        xStarting = (int)(x - 4)
        yStarting = (int)(4 - y)
        for x in range(xStarting, MAPWIDTH):
            for y in range(0, 9 - yStarting):
                drawTile(board[y][x], y + yStarting, x - xStarting)
    elif x <= 3 and (MAPHEIGHT - y) <= 5:
        xStarting = (int)(4 - x)
        yStarting = (int)(y - 4)
        for x in range(0, 9 - xStarting):
            for y in range(yStarting, MAPHEIGHT - 1):
                drawTile(board[y][x], y - yStarting, x + xStarting)
    elif (MAPWIDTH - x) <= 5 and (MAPHEIGHT - y) <= 5:
        xStarting = (int)(x - 4)
        yStarting = (int)(y - 4)
        for x in range(xStarting, MAPWIDTH):
            for y in range(yStarting, MAPHEIGHT - 1):
                drawTile(board[y][x], y - yStarting, x - xStarting)
    elif x <= 3:
        xStarting = (int)(4 - x)
        yStarting = (int)(y - 4)
        for x in range(0, 9 - xStarting):
            for y in range(yStarting, yStarting + 9):
                drawTile(board[y][x], y - yStarting, x + xStarting)
    elif y <= 3:
        xStarting = (int)(x - 4)
        yStarting = (int)(4 - y)
        for x in range(xStarting, xStarting + 9):
            for y in range(0, 9 - yStarting):
                drawTile(board[y][x], y + yStarting, x - xStarting)
    elif (MAPWIDTH - x) <= 5:
        xStarting = (int)(x - 4)
        yStarting = (int)(y - 4)
        for x in range(xStarting, MAPWIDTH):
            for y in range(yStarting, yStarting + 9):
                drawTile(board[y][x], y - yStarting, x - xStarting)
    elif (MAPHEIGHT - y) <= 5:
        xStarting = (int)(x - 4)
        yStarting = (int)(y - 4)
        for x in range(xStarting, xStarting + 9):
            for y in range(yStarting, MAPHEIGHT - 1):
                drawTile(board[y][x], y - yStarting, x - xStarting)
    else:
        xStarting = (int)(x - 4)
        yStarting = (int)(y - 4)
        for x in range(xStarting, xStarting + 9):
            for y in range(yStarting, yStarting + 9):
                drawTile(board[y][x], y - yStarting, x - xStarting)
    funkyBoi = pygame.image.load('FunkyMan.png')
    DISPLAYSURF.blit(funkyBoi, [369, 362])
    timeIm = BASICFONT.render(str(time), True, BLUE)
    DISPLAYSURF.blit(timeIm, (10, 10))
    i = 0
    for x in (inventory):
        left = i * 90
        top = 810
        pygame.draw.rect(DISPLAYSURF, DIMGRAY, (left, top, TILESIZE, TILESIZE))
        if x == "r":
            pygame.draw.circle(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                               (int)(TILESIZE / 8))
            pygame.draw.line(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                             (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
            pygame.draw.line(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
            pygame.draw.line(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
        if x == "o":
            pygame.draw.circle(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                               (int)(TILESIZE / 8))
            pygame.draw.line(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                             (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
            pygame.draw.line(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
            pygame.draw.line(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
        if x == "b":
            pygame.draw.circle(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                               (int)(TILESIZE / 8))
            pygame.draw.line(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                             (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
            pygame.draw.line(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
            pygame.draw.line(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
        if x == "g":
            pygame.draw.circle(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                               (int)(TILESIZE / 8))
            pygame.draw.line(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                             (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
            pygame.draw.line(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
            pygame.draw.line(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
        if x == "p":
            pygame.draw.circle(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                               (int)(TILESIZE / 8))
            pygame.draw.line(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                             (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
            pygame.draw.line(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
            pygame.draw.line(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                             (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
        if x == "C":
            pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
            bull = pygame.image.load('bulldozer.png')
            DISPLAYSURF.blit(bull, [left + 6, top + 15])
        if x == "S":
            pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
            scuba = pygame.image.load('scuba.png')
            DISPLAYSURF.blit(scuba, [left + 17, top])
        if x == "f":
            pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
            fireSuit = pygame.image.load('fireproof.png')
            DISPLAYSURF.blit(fireSuit, [left, top])
        if x == "i":
            pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
            ice = pygame.image.load('skate.png')
            DISPLAYSURF.blit(ice, [left + 5, top])
        if x == "h":
            pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
            shovel = pygame.image.load('shovel.png')
            DISPLAYSURF.blit(shovel, [left, top])
        pygame.draw.line(DISPLAYSURF, WHITE, (left, top), (left + TILESIZE, top), 5)
        pygame.draw.line(DISPLAYSURF, WHITE, (left, top), (left, top + TILESIZE), 5)
        pygame.draw.line(DISPLAYSURF, WHITE, (left + TILESIZE, top), (left + TILESIZE, top + TILESIZE), 5)
        pygame.draw.line(DISPLAYSURF, WHITE, (left, top + TILESIZE), (left + TILESIZE, top + TILESIZE), 5)
        i += 1
    if dead:
        pygame.draw.rect(DISPLAYSURF, BLACK, (140, 120, 540, 520))
        textSurf, textRect = makeText("You Died", WHITE, BLACK, 370, 300)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfTwo, textRectTwo = makeText("Press Space to Reset", WHITE, BLACK, 300, 400)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)
    if completed:
        pygame.draw.rect(DISPLAYSURF, BLACK, (140, 120, 540, 520))
        textSurf, textRect = makeText("You Made It!", WHITE, BLACK, 370, 300)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfTwo, textRectTwo = makeText("It took you", WHITE, BLACK, 305, 350)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)
        timeIm = BASICFONT.render(str(finishTime), True, WHITE)
        DISPLAYSURF.blit(timeIm, (415, 350))
        secondSurf, secondRect = makeText("seconds.", WHITE, BLACK, 455, 350)
        DISPLAYSURF.blit(secondSurf, secondRect)
        textSurfThree, textRectThree = makeText("Press Space to Move on to Next Level", WHITE, BLACK, 270, 400)
        DISPLAYSURF.blit(textSurfThree, textRectThree)
    if hint:
        pygame.draw.rect(DISPLAYSURF, BLACK, (140, 120, 540, 520))
        textSurf, textRect = makeText("Pick up the Bulldozer", WHITE, BLACK, 320, 300)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfTwo, textRectTwo = makeText("To Move the Wall Blocks With White Circles!", WHITE, BLACK, 200, 350)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)
        textSurfThree, textRectThree = makeText("These Blocks replace Water with Walking Blocks!", WHITE, BLACK, 180, 400)
        DISPLAYSURF.blit(textSurfThree, textRectThree)
    if win:
        pygame.draw.rect(DISPLAYSURF, BLACK, (140, 120, 540, 520))
        textSurf, textRect = makeText("You Made It!", WHITE, BLACK, 370, 300)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfTwo, textRectTwo = makeText("It took you", WHITE, BLACK, 305, 350)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)
        timeIm = BASICFONT.render(str(finishTime), True, WHITE)
        DISPLAYSURF.blit(timeIm, (415, 350))
        secondSurf, secondRect = makeText("seconds.", WHITE, BLACK, 455, 350)
        DISPLAYSURF.blit(secondSurf, secondRect)
        textSurfThree, textRectThree = makeText("Press Space to Exit", WHITE, BLACK, 320, 400)
        DISPLAYSURF.blit(textSurfThree, textRectThree)
    if lvl:
        board[oneY][oneX] = "N"
        board[twoY][twoX] = "N"
        board[threeY][threeX] = "N"
        board[fourY][fourX] = "N"
        board[fiveY][fiveX] = "N"
        board[sixY][sixX] = "N"

def makeText(text, color, bgcolor, top, left):
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def drawTile(block, yPos, xPos):
    left = xPos * 90
    top = yPos * 90
    if block == "N":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
    if block == "W":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
    if block == "H":
        water = pygame.image.load('water.png')
        DISPLAYSURF.blit(water, [left - 14, top - 14])
    if block == "F":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        fire = pygame.image.load('fire.png')
        DISPLAYSURF.blit(fire, [left, top])
    if block == "M":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, WHITE, (left + (int)(TILESIZE/2), top + (int)(TILESIZE/2)), (int)(TILESIZE/4))
    if block == "I":
        ice = pygame.image.load('ice.png')
        DISPLAYSURF.blit(ice, [left, top])
    if block == "D":
        dirt = pygame.image.load('dirt.png')
        DISPLAYSURF.blit(dirt, [left, top])
    if block == "r":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                           (int)(TILESIZE / 8))
        pygame.draw.line(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                         (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
        pygame.draw.line(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
        pygame.draw.line(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
    if block == "o":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                           (int)(TILESIZE / 8))
        pygame.draw.line(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                         (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
        pygame.draw.line(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
        pygame.draw.line(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
    if block == "b":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                           (int)(TILESIZE / 8))
        pygame.draw.line(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                         (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
        pygame.draw.line(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
        pygame.draw.line(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
    if block == "g":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                           (int)(TILESIZE / 8))
        pygame.draw.line(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                         (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
        pygame.draw.line(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
        pygame.draw.line(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
    if block == "p":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.75)),
                           (int)(TILESIZE / 8))
        pygame.draw.line(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.625)),
                         (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)), 5)
        pygame.draw.line(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 4)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE / 4)), 3)
        pygame.draw.line(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE * 0.35)),
                         (left + (int)(TILESIZE / 2.75), top + (int)(TILESIZE * 0.35)), 3)
    if block == "R":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 4), top),
                         (left + (int)(TILESIZE / 4), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 2), top),
                         (left + (int)(TILESIZE / 2), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE * 0.75), top),
                         (left + (int)(TILESIZE * 0.75), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + 5, top), (left + 5, top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + TILESIZE - 5, top), (left + TILESIZE - 5, top + TILESIZE), 4)
        pygame.draw.circle(DISPLAYSURF, RED, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 2)),
                           (int)(TILESIZE / 4))
    if block == "O":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 4), top),
                         (left + (int)(TILESIZE / 4), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 2), top),
                         (left + (int)(TILESIZE / 2), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE * 0.75), top),
                         (left + (int)(TILESIZE * 0.75), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + 5, top), (left + 5, top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + TILESIZE - 5, top), (left + TILESIZE - 5, top + TILESIZE), 4)
        pygame.draw.circle(DISPLAYSURF, ORANGE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 2)),
                           (int)(TILESIZE / 4))
    if block == "B":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 4), top),
                         (left + (int)(TILESIZE / 4), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 2), top),
                         (left + (int)(TILESIZE / 2), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE * 0.75), top),
                         (left + (int)(TILESIZE * 0.75), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + 5, top), (left + 5, top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + TILESIZE - 5, top), (left + TILESIZE - 5, top + TILESIZE), 4)
        pygame.draw.circle(DISPLAYSURF, BLUE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 2)),
                           (int)(TILESIZE / 4))
    if block == "G":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 4), top),
                         (left + (int)(TILESIZE / 4), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 2), top),
                         (left + (int)(TILESIZE / 2), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE * 0.75), top),
                         (left + (int)(TILESIZE * 0.75), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + 5, top), (left + 5, top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + TILESIZE - 5, top), (left + TILESIZE - 5, top + TILESIZE), 4)
        pygame.draw.circle(DISPLAYSURF, GREEN, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 2)),
                           (int)(TILESIZE / 4))
    if block == "P":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 4), top),
                         (left + (int)(TILESIZE / 4), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE / 2), top),
                         (left + (int)(TILESIZE / 2), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + (int)(TILESIZE * 0.75), top),
                         (left + (int)(TILESIZE * 0.75), top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + 5, top), (left + 5, top + TILESIZE), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (left + TILESIZE - 5, top), (left + TILESIZE - 5, top + TILESIZE), 4)
        pygame.draw.circle(DISPLAYSURF, PURPLE, (left + (int)(TILESIZE / 2), top + (int)(TILESIZE / 2)),
                           (int)(TILESIZE / 4))
    if block == "C":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        bull = pygame.image.load('bulldozer.png')
        DISPLAYSURF.blit(bull, [left + 6, top + 15])
    if block == "S":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        scuba = pygame.image.load('scuba.png')
        DISPLAYSURF.blit(scuba, [left + 17, top])
    if block == "f":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        fireSuit = pygame.image.load('fireproof.png')
        DISPLAYSURF.blit(fireSuit, [left, top])
    if block == "i":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        ice = pygame.image.load('skate.png')
        DISPLAYSURF.blit(ice, [left + 5, top])
    if block == "h":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        shovel = pygame.image.load('shovel.png')
        DISPLAYSURF.blit(shovel, [left, top])
    if block == "w":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        door = pygame.image.load('door.png')
        DISPLAYSURF.blit(door, [left, top])
    if block == "U":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        woodDoor = pygame.image.load('woodDoor.png')
        DISPLAYSURF.blit(woodDoor, [left, top])
    if block == "s":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.rect(DISPLAYSURF, CHARCOAL, (left + 5, top + 5, TILESIZE * 0.9, TILESIZE * 0.9))
        pygame.draw.line(DISPLAYSURF, WHITE, (left + TILESIZE * 0.25, top + TILESIZE *0.25), (left + TILESIZE * 0.25, top + TILESIZE *0.75), 4)
        pygame.draw.line(DISPLAYSURF, WHITE, (left + TILESIZE * 0.75, top + TILESIZE *0.25), (left + TILESIZE * 0.75, top + TILESIZE *0.75), 4)
        pygame.draw.line(DISPLAYSURF, WHITE, (left + TILESIZE * 0.25, top + TILESIZE *0.5), (left + TILESIZE * 0.75, top + TILESIZE *0.5), 4)
    if block == "Sprite":
        pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, TILESIZE, TILESIZE))
        fizzy = pygame.image.load('fizzy.png')
        DISPLAYSURF.blit(fizzy, [left, top])
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left, top), (left + TILESIZE, top), 3)
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left, top), (left, top + TILESIZE), 3)
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left + TILESIZE, top), (left + TILESIZE, top + TILESIZE), 3)
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left, top + TILESIZE), (left + TILESIZE, top + TILESIZE), 3)

if __name__ == '__main__':
    main()