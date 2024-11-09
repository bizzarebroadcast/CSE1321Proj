import pygame

class gameItem:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.rect = pygame.Rect(x, y, 20, 20)
        self.visible = True

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.screen, (255, 215, 0), self.rect)

    def collect(self):
        self.visible = False
