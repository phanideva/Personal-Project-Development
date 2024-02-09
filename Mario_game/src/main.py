import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from game_objects import Platform

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Mario-Type Game")

    # Set up the clock for FPS
    clock = pygame.time.Clock()

    # Create a sprite group for all sprites for easier management
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    # Create the player and add it to the sprite groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    all_sprites.add(player)

    # Create a platform and add it to the sprite groups
    platform = Platform(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, 200, 20)
    platforms.add(platform)
    all_sprites.add(platform)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player's velocity and position
        player.update(pressed_keys)

        # Collision detection
        player.on_ground = False  # Assume the player is not on the ground until we check collisions
        for platform in platforms:
            # Check for collision between the player and the platform
            if pygame.sprite.collide_rect(player, platform):
                # If the player is above the platform, correct the player's position and set on_ground to True
                if player.pos.y < platform.rect.top:
                    player.pos.y = platform.rect.top
                    player.vel.y = 0
                    player.on_ground = True
        
        # Drawing
        screen.fill((135, 206, 250))  # Fill the screen with a light blue color to represent the sky
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Update the display
        pygame.display.flip()

        # Cap the framerate at 60fps
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
