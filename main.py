import pygame

pygame.init()

winsize = (1024, 576)

screen = pygame.display.set_mode(winsize)
pygame.display.set_caption("2048")

main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False

pygame.QUIT