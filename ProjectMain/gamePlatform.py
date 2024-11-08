import pygame


class Platform:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rectPlat = pygame.Rect(int(x), int(y), int(width), int(height))
        #surf = pygame.Rect(width, height)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.rectPlat)



