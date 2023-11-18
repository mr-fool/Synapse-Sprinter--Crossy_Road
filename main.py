import sys
import pygame
import random
import sprites
import serial

arduino_port = 'COM3'
baud_rate = 115200
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

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
    received = False
    ser_out = [0.0,0.0]
    while not received:
        try:
            ser_out = ser.readline().decode().strip().split(',')
            if not len(ser_out) == 2:
                continue
            received = True
            ser_out = [float(i) for i in ser_out]
        except:
            continue

    # player_input_data = arduino_data.getdata()
    # if not player_input_data:
    #     continue
    # if not player_input_data[0]:
    #     continue
    # if not player_input_data[1]:
    #     continue
    # if not len(player_input_data) == 2:
    #     continue


    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # # Keydown events
        # elif event.type == pygame.KEYDOWN:
        #      if event.key == pygame.K_SPACE:
        #         player.move(-25)
        # # Keyup events
        # elif event.type == pygame.KEYUP:
        #     pass
    
    print(ser_out)
    sig1 = ser_out[0]
    sig2 = ser_out[1]
    if sig1 > 0 and sig2 > 0:
        player.move_y(-1)
    elif sig1 > 0:
        player.move_x(-1)
    elif sig2 > 0:
        player.move_x(1)

    # Clear the screen
    screen.fill(BLACK)
    player.update()
    player.draw(screen)


    # Update game state
    pygame.display.flip()
    clock.tick(60)