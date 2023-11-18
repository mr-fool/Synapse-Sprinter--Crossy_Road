import sys
import pygame
import random
import sprites
import arduino_data

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arduino Crossy Road")

# Primary colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Camera
cam_x = 0
cam_y = 0

# Player setup
player = sprites.Player(WIDTH//2, HEIGHT//2, 25, 25)


clock = pygame.time.Clock()


while True:
    player_input_data = arduino_data.getdata()
    if not player_input_data:
        continue
    if not player_input_data[0]:
        continue
    if not player_input_data[1]:
        continue
    if not len(player_input_data) == 2:
        continue

    cam_y += 1


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
    
    print(player_input_data)
    
    if float(player_input_data[0]) > 0:
        player.move(-25)

    # Clear the screen
    screen.fill(BLACK)
    player.update(cam_x, cam_y)
    player.draw(screen)


    # Update game state
    pygame.display.flip()
    clock.tick(60)