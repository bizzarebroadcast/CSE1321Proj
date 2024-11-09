import pygame
import sys
from gameChar import gameChar
from gamePlatform import Platform
pygame.init()

#hello

screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Funny Game")

blue = (0, 0, 255)
black = (0, 0, 0)

char = gameChar(800, 750, screen)


def platforms(screen):
    return [
        Platform(100, 700, 150, 20, screen),
        Platform(300, 600, 150, 20, screen),
        Platform(550, 500, 150, 20, screen),
        Platform(800, 400, 150, 20, screen),
        Platform(1000, 300, 150, 20, screen),
        Platform(200, 500, 120, 20, screen),
        Platform(450, 400, 120, 20, screen),
        Platform(700, 300, 120, 20, screen),
        Platform(950, 200, 120, 20, screen),
        Platform(1150, 100, 120, 20, screen)
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
        platRect = plat.rectPlat
        charRect = char.rectMod
        if charRect.colliderect(platRect):
            if charRect.bottom <= platRect.top + 20 and char.rectMod.y < platRect.y:
                char.rectMod.y = platRect.top - charRect.height+5
                char.yVel = 0
                grounded=True

        plat.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()