import pygame
from settings import GRAVITY, JUMP_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((40, 50))
        self.surf.fill((255, 0, 0))  # Red color for the player
        self.rect = self.surf.get_rect(center=(x, y))
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False

    def update(self, pressed_keys):
        self.vel.x = 0
        if pressed_keys[pygame.K_LEFT]:
            self.vel.x = -5
        if pressed_keys[pygame.K_RIGHT]:
            self.vel.x = 5
        
        self.vel.y += GRAVITY  # Apply gravity
        if self.on_ground and pressed_keys[pygame.K_SPACE]:
            self.vel.y = JUMP_HEIGHT  # Apply jump
        
        self.pos += self.vel
        self.rect.midbottom = self.pos

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
