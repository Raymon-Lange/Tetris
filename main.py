import pygame,sys
from grid import Grid
from blocks import *

pygame.init()
darkBlue = (44,44,127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

gameGrid = Grid()

block = TBlock()


gameGrid.printGrid()

while True:
    # STEP: Check for input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # STEP: Update postion 

    # STEP: Draw
    screen.fill(darkBlue)
    gameGrid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)