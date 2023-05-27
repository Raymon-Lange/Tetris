import pygame,sys

pygame.init()
darkBlue = (44,44,127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    # STEP: Check for input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # STEP: Update postion 

    # STEP: Draw

    screen.fill(darkBlue)
    pygame.display.update()
    clock.tick(60)