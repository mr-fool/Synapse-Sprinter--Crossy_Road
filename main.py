import sys
import pygame
import random
import sprites

# For dev
USING_ARDUINO = False

if USING_ARDUINO:
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

# Enemy setup
enemies = []


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Keydown events
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE and not USING_ARDUINO:
                player.move(-25)
        # Keyup events
        elif event.type == pygame.KEYUP:
            pass

    
    if USING_ARDUINO:
        player_input_data = arduino_data.getdata()
        if not player_input_data:
            continue
        if not player_input_data[0]:
            continue
        if not player_input_data[1]:
            continue
        if not len(player_input_data) == 2:
            continue

        
    # Clear the screen
    screen.fill(BLACK)

    # Camera control
    cam_y += 1
    print(cam_y)

    # Spawn enemies
    if cam_y%10 == 0 and random.randint(0, 10) < 1:
        size = 50
        x = random.randint(size, WIDTH-size)
        y = -100
        speed = random.randint(1, 10)
        enemy = sprites.Enemy(x, y, size, size, speed)
        enemies.append(enemy)
    
    if USING_ARDUINO:
        print(player_input_data)
        
        if float(player_input_data[0]) > 0:
            player.move(-25)
    
    for enemy in enemies:
        enemy.move()
        enemy.update(cam_x, cam_y)
        enemy.draw(screen)

    player.update(cam_x, cam_y)
    player.draw(screen)


    # Update game state
    pygame.display.flip()
    clock.tick(60)