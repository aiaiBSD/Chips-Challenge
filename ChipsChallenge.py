import pygame, sys, random, time
from pygame.locals import *
from pygame.font import *

with open('CCLvl1.txt') as lvlOne:
    linesOne = [line.split() for line in lvlOne]

BOARDWIDTH = 9
BOARDHEIGHT = 9
MAPHEIGHT = len(linesOne)
MAPWIDTH = len(linesOne[0])
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
FLAME = (226, 88, 34)
ICEBLUE = (165, 242, 243)
DIRT = (124, 94, 66)
DIMGRAY = (64, 64, 64)
ORANGE = (255, 165, 0)

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

    nxtLvl = False
    mainBoard = []
    for x in range(MAPWIDTH):
        mainBoard.append(linesOne[x])

    mapY = (int)(MAPHEIGHT/2 - 1)
    mapX = (int)(MAPWIDTH/2)
    inventory = []
    for x in range(0, 9):
        inventory.append("E")

    dead = False

    while True:
        drawBoard(mainBoard, nxtLvl, mapX, mapY, inventory, dead)

        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key in (K_LEFT, K_a) and not dead:
                    if not mainBoard[mapX - 1][mapY] == "W" and not mainBoard[mapY][mapX - 1] == "R" and not mainBoard[mapY][mapX - 1] == "O" and not mainBoard[mapY][mapX - 1] == "B" and not mainBoard[mapY][mapX - 1] == "P" and not mainBoard[mapY][mapX - 1] == "G":
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
                if event.key in (K_RIGHT, K_d) and not dead:
                    if not mainBoard[mapX + 1][mapY] == "W" and not mainBoard[mapY][mapX + 1] == "R" and not mainBoard[mapY][mapX + 1] == "O" and not mainBoard[mapY][mapX + 1] == "B" and not mainBoard[mapY][mapX + 1] == "P" and not mainBoard[mapY][mapX + 1] == "G":
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
                if event.key in (K_UP, K_w) and not dead:
                    if not mainBoard[mapX][mapY - 1] == "W" and not mainBoard[mapY - 1][mapX] == "R" and not mainBoard[mapY - 1][mapX] == "O" and not mainBoard[mapY - 1][mapX] == "B" and not mainBoard[mapY - 1][mapX] == "P" and not mainBoard[mapY - 1][mapX] == "G":
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
                if event.key in (K_DOWN, K_s) and not dead:
                    if not mainBoard[mapX][mapY + 1] == "W" and not mainBoard[mapY + 1][mapX] == "R" and not mainBoard[mapY + 1][mapX] == "O" and not mainBoard[mapY + 1][mapX] == "B" and not mainBoard[mapY + 1][mapX] == "P" and not mainBoard[mapY + 1][mapX] == "G":
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
                if event.key in (K_SPACE, K_x) and dead:
                    for x in range(MAPWIDTH):
                        mainBoard[x] = linesOne[x]
                    for x in range(0, 9):
                        inventory[x] = "E"
                    mapY = (int)(MAPHEIGHT / 2 - 1)
                    mapX = (int)(MAPWIDTH / 2)
                    dead = False

        if checkDie(mainBoard[mapY][mapX], inventory):
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

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def checkDie(block, invent):
    water = False
    fire = False
    for item in invent:
        if item == "S":
            water = True
        if item == "f":
            fire = True
    if block == "H" and not water:
        return True
    if block == "F" and not fire:
        return True
    return False

def terminate():
    pygame.quit()
    sys.exit()

def drawBoard(board, lvl, x, y, inventory, dead):
    DISPLAYSURF.fill(BLACK)
    if lvl == False:
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
        pygame.draw.rect(DISPLAYSURF, SEABLUE, (left, top, TILESIZE, TILESIZE))
    if block == "F":
        pygame.draw.rect(DISPLAYSURF, FLAME, (left, top, TILESIZE, TILESIZE))
    if block == "M":
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, TILESIZE, TILESIZE))
        pygame.draw.circle(DISPLAYSURF, WHITE, (left + (int)(TILESIZE/2), top + (int)(TILESIZE/2)), (int)(TILESIZE/4))
    if block == "I":
        pygame.draw.rect(DISPLAYSURF, ICEBLUE, (left, top, TILESIZE, TILESIZE))
    if block == "D":
        pygame.draw.rect(DISPLAYSURF, DIRT, (left, top, TILESIZE, TILESIZE))
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
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left, top), (left + TILESIZE, top), 3)
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left, top), (left, top + TILESIZE), 3)
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left + TILESIZE, top), (left + TILESIZE, top + TILESIZE), 3)
    pygame.draw.line(DISPLAYSURF, DARKGRAY, (left, top + TILESIZE), (left + TILESIZE, top + TILESIZE), 3)

if __name__ == '__main__':
    main()