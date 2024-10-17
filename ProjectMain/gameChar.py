import pygame
import sys

class gameChar():
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.jumping = False
        self.yVel = 0
        self.pressed_keys = pygame.key.get_pressed()
    def draw(self):
        pygame.draw.rect(self.screen,(255, 0, 0),(self.x, self.y, 50, 50))
        print(str(self.x)+ " , " + str(self.y))
    def move(self, pressed_keys):
        if pressed_keys[pygame.K_d] and self.x <= 1400:
            self.x += 5
        if pressed_keys[pygame.K_a] and self.x >= 0:
            self.x -= 5
        if pressed_keys[pygame.K_SPACE] and self.jumping == False:
            self.jumping = True
            self.yVel = 20
            self.y -= 1
            print("jump")
        if self.jumping == True:
            if self.y - self.yVel > 750:
                self.y = 750
                self.yVel = 0
                self.jumping = False
            elif self.y <= 750:
                self.y -= self.yVel
            self.yVel -= 1



