import pygame, random, numpy

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#set winsize
winsize = (400, 500)

#screen var
screen = pygame.display.set_mode(winsize)
gridGUI = pygame.image.load("assets\\Grid.png").convert()
font = pygame.font.SysFont("Impact", 35)
numbersFont = pygame.font.SysFont("Impact", 40)

#window name
pygame.display.set_caption("2048")

#general vars
moves = 0

#game grid in a 2d array
grid = numpy.array([[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]])

#define the first position
def RandPos():
    return numpy.array([random.randint(0,3), random.randint(0,3)])

#update moves every move
def UpdateMoves():
    global moves
    moves += 1

#show moves on screen
def ShowMoves(x, y):
    movesTEXT = font.render("Moves: " + str(moves), 1, (63.2,15.1,0))
    screen.blit(movesTEXT, (x, y))

#print numbers on gui
def printNumberGUI(x,y):
    number = numbersFont.render(str(2), 1, (63.2,15.1,0))
    screen.blit(number, (x, y))

#update value of grid 
def UpdateValueGrid():
    for i in range(100):
        temp = RandPos()
        if grid[temp[0], temp[1]] == 0:
            grid[temp[0], temp[1]] = 2
            break
    print(grid)

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

#move numbers (WIP)
def moveNumberCode():
    temp = getInput() 
    temp1 = 0
    z = 1
    match temp:
        case 1:
            for x in range(4):
                for y in range(4):
                    if grid[[x],[y]] != 0:
                        if y != 0:
                            while z < y:
                                print("1")
                                if grid[[x],[y - z]] == 0:
                                    print("2")
                                    grid[[x],[y - z + 1]] = grid[[x],[y]]
                                    grid[[x],[y]] = 0
                                    break
                                z += 1
                                


#move numbers on GUI 
def moveNumbersGUI():
    for x in range(4):
        for y in range(4):
            if grid[[x],[y]] != 0:
                printNumberGUI(100 * (y + 1) - 50, (100 * (x + 1) - 50) + 100 )

#show grid 
def ShowGUI(x, y):
    screen.blit(gridGUI, (x, y))

#screen update every frame
def updateScreen():
    screen.fill((0,0,0))
    ShowGUI(0, 100)
    ShowMoves(10,30)
    moveNumbersGUI()

    pygame.display.update()
    #lock framerate to 60
    clock.tick(60)

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
        if getInput() != 0:
            moveNumberCode()
            UpdateValueGrid()
            UpdateMoves()
            
    Debug()
    updateScreen()

pygame.QUIT