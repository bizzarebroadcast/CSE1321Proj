import pygame, sys
from pygame.locals import *


pygame.init()

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

game_started = False

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (event.type == QUIT):
            sys.exit(0)
        if (keys[pygame.K_ESCAPE]):
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                game_started = True
    
    screen.fill((0, 0, 0))

    if (game_started == False):
        rect1 = pygame.Rect(200, 400, 100, 45)
        surf1 = pygame.Surface((rect1.width, rect1.height))
        surf1.fill((0, 255, 0))

        font = pygame.font.Font(None, 25)
        startGame = font.render("Start Game!", True, (0, 0, 0))
        right = font.render("Press D to move right", True, (0, 255, 0))
        left = font.render("Press A to move left", True, (0, 255, 0))

        screen.blit(surf1, (rect1.x, rect1.y))
        screen.blit(startGame, (200, 414))
        screen.blit(right, (300, 200))
        screen.blit(left, (26.5, 200))

    else:
        font = pygame.font.Font(None, 36)
        game_text = font.render("Game Started!", True, (255, 255, 255))
        screen.blit(game_text, (150, 250))

    pygame.display.flip()
    clock.tick(60)
