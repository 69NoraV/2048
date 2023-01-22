import pygame, random, numpy

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
grid = numpy.array([[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]])

#define the first position
def RandPos():
    return numpy.array([random.randint(0,3), random.randint(0,3)])

#update score every move
def UpdateScore():
    global score
    score += 1

#update value of grid (WIP)
def UpdateValueGrid():
    for i in range(100):
        temp = RandPos()
        if grid[temp[0], temp[1]] == 0:
            grid[temp[0], temp[1]] = 2
            break

#get input player
def getInput():
    if pygame.key.get_pressed()[pygame.K_UP]:
        return 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        return 2
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        return 3
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        return 4
    
    return 0

def moveNumbers():
    pass

#show grid (WIP)
def ShowGrid():
    pass

#debug function
def Debug():
    pass

#main loop
main = True
while main:
    #get every event of the player
    for event in pygame.event.get():
        #if the event is quit then quit
        if event.type == pygame.QUIT:
            main = False
        getInput()
        if getInput() != 0:
            UpdateValueGrid()
            UpdateScore()
    Debug()
pygame.QUIT