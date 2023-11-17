import sys
import pygame
import random
import sprites

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arduino Crossy Road")

# Primary colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player setup
player = sprites.Player(WIDTH//2, HEIGHT//2, 25, 25)


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Keydown events
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                player.move(-25)
        # Keyup events
        elif event.type == pygame.KEYUP:
            pass

    # Clear the screen
    screen.fill(BLACK)
    player.update()
    player.draw(screen)


    # Update game state
    pygame.display.flip()
    clock.tick(60)