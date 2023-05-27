import pygame,sys
from game import Game



pygame.init()
darkBlue = (44,44,127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    # STEP: Check for input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game.gameOver == False:
            if event.key == pygame.K_LEFT:
                game.moveLeft()
            if event.key == pygame.K_RIGHT:
                game.moveRight()
            if event.key == pygame.K_UP:
                game.rotateBlock()
            if event.key == pygame.K_DOWN:
                game.moveDown()
        if event.type == GAME_UPDATE and game.gameOver == False:
            game.moveDown()


    # STEP: Draw
    screen.fill(darkBlue)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)