import pygame
import sys

class gameChar():
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.yVel = 0
        self.grounded = False
        self.pressed_keys = pygame.key.get_pressed()
        #quick fix
        self.rectMod = pygame.Rect(x, y, 50, 50)
    def draw(self):
        pygame.draw.rect(self.screen,(255, 0, 0),(self.rectMod.x, self.rectMod.y, 50, 50))
        #print(str(self.rectMod.x)+ " , " + str(self.rectMod.y))
    def move(self, pressed_keys):
        if pressed_keys[pygame.K_d] and self.rectMod.x <= 1350:
            self.rectMod.x += 5
        if pressed_keys[pygame.K_a] and self.rectMod.x >= 0:
            self.rectMod.x -= 5
        if pressed_keys[pygame.K_SPACE]:
            self.yVel = 20
            self.rectMod.y -= 1
            print("jump")
        if not self.grounded:
            if self.rectMod.y - self.yVel > 750:
                self.rectMod.y = 750
                self.yVel = 0
            elif self.rectMod.y <= 750:
                self.rectMod.y -= self.yVel
            self.yVel -= 1
    def setgrounded (self, grounded):
        self.grounded = grounded





