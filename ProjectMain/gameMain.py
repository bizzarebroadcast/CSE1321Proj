import pygame, sys
from pygame.locals import *
from gameChar import gameChar
from gamePlatform import Platform
from gameItem import gameItem

pygame.init()

background_music = pygame.mixer.Sound('BG Music.mp3')
victory_sound = pygame.mixer.Sound('HW Victory.mp3')
loss_sound = pygame.mixer.Sound('gameLoss.mp3')
land_sound = pygame.mixer.Sound('land.wav')
resolution = (500, 500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

game_started = False
gameRunning = True
gameWin = False
gameLoss = False

while gameRunning:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
            gameRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                game_started = True
                background_music.play(-1)

    screen.fill((0, 0, 0))

    if not game_started:
        background_music.stop()

        rect1 = pygame.Rect(200, 400, 100, 45)
        surf1 = pygame.Surface((rect1.width, rect1.height))
        surf1.fill((0, 255, 0))

        font = pygame.font.Font(None, 25)
        startGame = font.render("Start Game!", True, (0, 0, 0))
        top = font.render("Collect the coin before the timer runs out!", True, (0, 255, 0))
        right = font.render("Press D to move right", True, (0, 255, 0))
        left = font.render("Press A to move left", True, (0, 255, 0))
        bottom = font.render("Press Space to Jump", True, (0, 255, 0))
        esc = font.render("Press ESC button to close game", True, (0, 255, 0))

        screen.blit(surf1, (rect1.x, rect1.y))
        screen.blit(top, (80, 100))
        screen.blit(startGame, (200, 414))
        screen.blit(right, (300, 200))
        screen.blit(left, (26.5, 200))
        screen.blit(bottom, (175, 300))
        screen.blit(esc, (130, 350))
    elif gameWin:
        background_music.stop()

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
        if pressed_keys[pygame.K_r]:
            gameWin = False
            sound_played = False
            background_music.play(-1)
    elif gameLoss:
        background_music.stop()

        screen.fill((0, 0, 0))
        rect2 = pygame.Rect(200, 400, 900, 350)
        surf1 = pygame.Surface((rect2.width, rect2.height))
        surf1.fill((255, 255, 255))
        font = pygame.font.Font(None, 200)
        font2 = pygame.font.Font(None, 90)
        font3 = pygame.font.Font(None, 50)
        winGame = font.render("You lost :(", True, (0, 255, 0))
        winTxt = font2.render("Try again next time!", True, (255, 192, 203))
        reset = font3.render("Press R to restart", True, (255, 0, 0))
        screen.blit(surf1, (rect2.x, rect2.y))
        screen.blit(winGame, (350, 500))
        screen.blit(winTxt, (352, 650))
        screen.blit(reset, (352, 450))
        if pressed_keys[pygame.K_r]:
            gameLoss = False
            sound_played = False
            background_music.play(-1)
    else:
        screen = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption("Funny Game")

        blue = (0, 0, 255)
        black = (0, 0, 0)

        char = gameChar(800, 750, screen)

        def platforms(screen):
            return [
                Platform(1150, 700, 150, 20, screen),
                Platform(1000, 600, 150, 20, screen),
                Platform(760, 530, 150, 20, screen),
                Platform(590, 650, 150, 20, screen),
                Platform(330, 620, 150, 20, screen),
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
        landing_played = False
        timer_duration = 30
        start_ticks = pygame.time.get_ticks()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gameRunning = False  # Exit outer loop too
                pressed_keys = pygame.key.get_pressed()
            screen.fill(black)
            char.move(pressed_keys)
            char.draw()
            char.setgrounded(False)

            for plat in platform_list:
                platRect = plat.rectPlat
                charRect = char.rectMod
                if charRect.colliderect(platRect):
                    if charRect.bottom <= platRect.top + 20 and char.rectMod.y < platRect.y and char.yVel <= 0:
                        char.rectMod.y = platRect.top - charRect.height + 2
                        char.setgrounded(True)
                        if not landing_played:
                            land_sound.play()
                            landing_played = True
                    else:
                        landing_played = False
                plat.draw()

            if item.visible:
                if char.rectMod.colliderect(item.rect):
                    item.collect()
                    if not sound_played:
                        victory_sound.play()
                        sound_played = True

            item.draw()

            seconds = timer_duration - (pygame.time.get_ticks() - start_ticks) // 1000


            font = pygame.font.Font(None, 40)
            timer_text = font.render(f"Time Left: {seconds}", True, (255, 255, 255))
            screen.blit(timer_text, (10, 10))

            if seconds <= 0:
                loss_sound.play()
                gameLoss = True
                running = False
            if char.rectMod.colliderect(item.rect):
                gameWin = True
                running = False

            pygame.display.update()
            clock.tick(30)
    pygame.display.flip()
    clock.tick(60)
