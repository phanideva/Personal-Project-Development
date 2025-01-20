import pygame
import sys
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dangerous Dave Clone")

# Load images
player_img = pygame.image.load(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\images\\player.png")
brick_block_img = pygame.image.load(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\images\\brick_block.png")
gem_img = pygame.image.load(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\images\\gem.png")
fire_img = pygame.image.load(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\images\\fire.png")
door_img = pygame.image.load(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\images\\door.png")
background_img = pygame.image.load(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\images\\background.png")

# Load sounds
jump_sound = pygame.mixer.Sound(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\sounds\\jump.wav")
game_over_sound = pygame.mixer.Sound(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\sounds\\game_over.wav")
coin_sound = pygame.mixer.Sound(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\sounds\\coin.wav")
win_sound = pygame.mixer.Sound(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\sounds\\win.wav")
burn_sound = pygame.mixer.Sound(r"C:\\Users\\phani\\Python practice\\dave_game\\assets\\sounds\\burn.wav")

# Player settings
player_speed = 5
gravitational_pull = 0.5
jump_height = -12
lives = 5
score = 0

# Current level
default_level = 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT - 100)
        self.vel_y = 0
        self.on_ground = False

    def update(self, blocks):
        keys = pygame.key.get_pressed()
        
        if keys[K_LEFT]:
            self.rect.x -= player_speed
        if keys[K_RIGHT]:
            self.rect.x += player_speed
        if keys[K_SPACE] and self.on_ground:
            self.vel_y = jump_height
            self.on_ground = False
            jump_sound.play()
        
        # Gravity
        self.vel_y += gravitational_pull
        self.rect.y += self.vel_y
        
        # Collision with blocks
        self.on_ground = False
        for block in blocks:
            if self.rect.colliderect(block.rect) and self.vel_y >= 0:
                self.rect.bottom = block.rect.top
                self.vel_y = 0
                self.on_ground = True

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = brick_block_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = gem_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = fire_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = door_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Create sprite groups
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

def create_level(level):
    block_group = pygame.sprite.Group()
    gem_group = pygame.sprite.Group()
    fire_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()

    if level == 1:
        # Level 1 Maze Design (Exact from Image)
        blocks = [
            (100, 500), (150, 500), (200, 500), (250, 500), (300, 500),
            (350, 500), (400, 500), (450, 500), (500, 500), (550, 500),
            (600, 500), (650, 500), (700, 500),
            (200, 400), (400, 400), (600, 400),
            (200, 300), (400, 300), (600, 300),
            (100, 200), (700, 200)
        ]
        gems = [(150, 450), (350, 450), (550, 450)]
        fire_positions = [(300, 550), (500, 550)]
        door = Door(700, 150)

    elif level == 2:
        blocks = [
            (100, 500), (200, 500), (300, 500), (400, 500),
            (100, 400), (300, 400), (500, 400),
            (100, 300), (200, 300), (400, 300), (600, 300),
            (700, 200)
        ]
        gems = [(200, 450), (350, 350), (500, 450)]
        fire_positions = [(300, 550)]
        door = Door(700, 150)

    for pos in blocks:
        block_group.add(Block(*pos))
    
    for pos in gems:
        gem_group.add(Gem(*pos))
    
    for pos in fire_positions:
        fire_group.add(Fire(*pos))
    
    door_group.add(door)
    return block_group, gem_group, fire_group, door_group

def main_menu():
    while True:
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 48)
        title_text = font.render("Dangerous Dave Clone", True, WHITE)
        start_text = font.render("Press ENTER to Start", True, WHITE)
        exit_text = font.render("Press ESC to Exit", True, WHITE)
        
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 200))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 300))
        screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 400))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                return

def main():
    global lives, score, default_level
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont(None, 36)
    block_group, gem_group, fire_group, door_group = create_level(default_level)
    
    while running:
        screen.blit(background_img, (0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        player_group.update(block_group)

        # Check for fire collision
        if pygame.sprite.spritecollide(player, fire_group, False):
            burn_sound.play()
            lives -= 1
            player.rect.center = (100, HEIGHT - 100)
            if lives == 0:
                game_over_sound.play()
                main_menu()
                return

        # Check for gem collection
        collected_gems = pygame.sprite.spritecollide(player, gem_group, True)
        for gem in collected_gems:
            coin_sound.play()
            score += 10

        # Check if player reaches the door
        if pygame.sprite.spritecollide(player, door_group, False):
            win_sound.play()
            default_level += 1
            block_group, gem_group, fire_group, door_group = create_level(default_level)
            player.rect.center = (100, HEIGHT - 100)
        
        player_group.draw(screen)
        block_group.draw(screen)
        gem_group.draw(screen)
        fire_group.draw(screen)
        door_group.draw(screen)
        
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()
    main()