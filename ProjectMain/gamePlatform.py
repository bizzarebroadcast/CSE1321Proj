import pygame

class platform:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

def platforms(screen):
    return [
        platform(200, 650, 200, 20, screen),
        platform(500, 550, 200, 20, screen),
        platform(800, 450, 200, 20, screen),
        platform(1100, 350, 200, 20, screen),
        platform(300, 250, 200, 20, screen)
    ]
