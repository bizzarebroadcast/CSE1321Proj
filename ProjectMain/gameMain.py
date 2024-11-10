import pygame, sys
from pygame.locals import *
from gameChar import gameChar
from gamePlatform import Platform
from gameItem import gameItem

pygame.init()

victory_sound = pygame.mixer.Sound('HW Victory.mp3')

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
        item = gameItem(1200, 80, screen)

        running = True
        sound_played = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(black)
            pressed_keys = pygame.key.get_pressed()
            char.move(pressed_keys)
            char.draw()
            char.setgrounded(False)

            for plat in platform_list:
                platRect = plat.rectPlat
                charRect = char.rectMod
                if charRect.colliderect(platRect):
                    if charRect.bottom <= platRect.top + 20 and char.rectMod.y < platRect.y and char.yVel <= 0:
                        char.rectMod.y= platRect.top-charRect.height+2
                        char.setgrounded(True)
                plat.draw()

            if item.visible:
                if char.rectMod.colliderect(item.rect):
                    item.collect()
                    if not sound_played:
                        victory_sound.play()
                        sound_played = True

            item.draw()

            if char.rectMod.colliderect(item.rect):
                screen.fill((0, 0, 0))
                rect2 = pygame.Rect(200, 400, 900, 350)
                surf1 = pygame.Surface((rect2.width, rect2.height))
                surf1.fill((255, 255, 255))
                font = pygame.font.Font(None, 200)
                font2 = pygame.font.Font(None, 90)
                font3 = pygame.font.Font(None, 50)
                winGame = font.render("You Won!", True, (0, 255, 0))
                winTxt = font2.render("Congrats!! :D", True, (255, 192, 203))
                reset = font3.render("Press R to restart", True, (255, 0, 0))
                screen.blit(surf1, (rect2.x, rect2.y))
                screen.blit(winGame, (350, 500))
                screen.blit(winTxt, (352, 650))
                screen.blit(reset, (352, 450))

            pygame.display.update()
            clock.tick(30)

        pygame.quit()

    pygame.display.flip()
    clock.tick(60)
