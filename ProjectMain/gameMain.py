import pygame
import sys
from gameChar import gameChar
from gamePlatform import Platform
pygame.init()

#hello

screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Funny Game")

blue = (0, 0, 255)
black = (0, 0, 0)

char = gameChar(800, 750, screen)


def platforms(self):
    return [
        Platform(200, 650, 200, 20, screen),
        Platform(500, 550, 200, 20, screen),
        Platform(800, 450, 200, 20, screen),
        Platform(1100, 350, 200, 20, screen),
        Platform(300, 250, 200, 20, screen)
    ]

platform_list = platforms(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pressed_keys = pygame.key.get_pressed()
    char.move(pressed_keys)
    char.draw()

    for plat in platform_list:
        plat.draw()

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
