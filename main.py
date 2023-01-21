import pygame, random

#initialize pygame
pygame.init()

#set winsize
winsize = (1024, 576)

#standard var
screen = pygame.display.set_mode(winsize)

#window name
pygame.display.set_caption("2048")

#general vars
score = 0

#game grid in a 2d array
grid = [[0,0,0,1],
        [0,0,1,0],
        [0,1,0,0],
        [0,0,0,1]]

#define the first position
def randPos():
    posX = random.randint(0,3)
    posY = random.randint(0,3)
    return {posX, posY}

#update score every move
def updateScore():
    score += 1

#update value of grid (WIP)
def updateValueGrid():
    while 1:
        temp = randPos()
        if grid[temp] == 0:
            grid[temp] = 1
            break



#show grid (WIP)
def showGrid():
    pass

#debug function
def debug():
    pass

#main loop
main = True
while main:
    #get every event of the player
    for event in pygame.event.get():
        #if the event is quit then quit
        if event.type == pygame.QUIT:
            main = False
    
    debug()
pygame.QUIT