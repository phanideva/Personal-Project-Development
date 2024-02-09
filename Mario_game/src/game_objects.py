import pygame
from settings import SCREEN_WIDTH

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((106, 55, 5))  # Brown color for platforms
        self.rect = self.surf.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

# You can extend this file by adding more classes for different types of game objects.
# For example, items the player can collect, or obstacles that move or have special interactions.
