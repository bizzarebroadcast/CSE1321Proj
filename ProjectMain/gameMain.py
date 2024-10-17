import pygame
import sys
from gameChar import gameChar

pygame.init()

screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Funny Game")

blue = (0,0,255)
black = (0,0,0)

running = True

char = gameChar(800, 750, screen)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pressed_keys = pygame.key.get_pressed()
    char.move(pressed_keys)
    char.draw()
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()