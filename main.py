import pygame,sys
from game import Game
from colors import Colors


pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
lines_cleared = title_font.render("Lines", True, Colors.white)
level_on = title_font.render("Level", True, Colors.white)


scoreBox = pygame.Rect(320, 295, 170, 50)
linesBox = pygame.Rect(320, 380, 170, 50)
levelBox = pygame.Rect(320, 465, 170, 50)
nextBox = pygame.Rect( 320, 55, 170, 120)

screen = pygame.display.set_mode((500,620))
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
        if event.type == pygame.KEYDOWN :
            if game.gameOver == True:
                game.gameOver = False
                game.reset()
            if event.key == pygame.K_LEFT and game.gameOver == False:
                game.moveLeft()
            if event.key == pygame.K_RIGHT and game.gameOver == False:
                game.moveRight()
            if event.key == pygame.K_UP and game.gameOver == False:
                game.rotateBlock()
            if event.key == pygame.K_DOWN and game.gameOver == False:
                game.moveDown()
        if event.type == GAME_UPDATE and game.gameOver == False:
            game.moveDown()


    # STEP: Draw
    screen.fill(Colors.dark_blue)
    
    screen.blit(score_surface, (365, 265, 50, 50))
    screen.blit(next_surface, (375, 20, 50, 50))
    screen.blit(lines_cleared, (365, 350, 50, 50))
    screen.blit(level_on, (365, 435, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, nextBox, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, scoreBox, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, linesBox, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, levelBox, 0, 10)

    linesValueSurface = title_font.render(str(game.linesClear), True, Colors.white)
    screen.blit(linesValueSurface, linesValueSurface.get_rect(centerx = linesBox.centerx, 
		centery = linesBox.centery))
    
    scoreValueSurface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(scoreValueSurface, linesValueSurface.get_rect(centerx = scoreBox.centerx, 
		centery = scoreBox.centery))
    
    levelValueSurface = title_font.render(str(game.level), True, Colors.white)
    screen.blit(levelValueSurface, levelValueSurface.get_rect(centerx = levelBox.centerx, 
		centery = levelBox.centery))
    
    game.draw(screen)

    if game.gameOver == True:
        screen.blit(game_over_surface, (90, 450, 50, 50))


    pygame.display.update()
    clock.tick(60)