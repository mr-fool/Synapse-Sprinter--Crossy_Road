import pygame

class Player:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0, 128, 255)

    def move_x(self, amount):
        self.rect.x += amount
    
    def move_y(self, amount):
        self.rect.y += amount

    def update(self):
        pass
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)