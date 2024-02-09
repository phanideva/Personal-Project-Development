import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((30, 40))
        self.surf.fill((0, 0, 255))  # Blue color for the enemy
        self.rect = self.surf.get_rect(center=(x, y))

    def update(self):
        # Add movement or other behavior here
        pass

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
