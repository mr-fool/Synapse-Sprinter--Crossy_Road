import sys
import pygame
import random
import sprites
import serial
import threading

arduino_port = 'COM3'
baud_rate = 115200
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
breaking_case = False
sig1 = 0
sig2 = 0

def arduino_data():
# This function is going to keep running and fetch data from the arduino
    global sig1, sig2
    while not breaking_case:
        received = False
        while not received:
            try:
                ser_out = ser.readline().decode().strip().split(',')
                if not len(ser_out) == 2:
                    continue
                else:
                    received = True
                    sig1 = float(ser_out[0])
                    sig2 = float(ser_out[1])
            except Exception as e:  
                sig1 = 0
                sig2 = 0
                continue

arduino_data_thread = threading.Thread(target=arduino_data, daemon=True)
arduino_data_thread.start()

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

    print(f"left: {sig1}, right: {sig2}")
    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Quitting py game")
            ser.close()
            print("closing serial connection")
            print("Exiting...")
            sys.exit()
    
    if sig1 > 0 and sig2 > 0:
        print("forward")
        player.move_y(-1)
    elif sig1 > 0:
        print("left")
        player.move_x(-1)
    elif sig2 > 0:
        print("right")
        player.move_x(1)

    # Clear the screen
    screen.fill(BLACK)
    player.update()
    player.draw(screen)


    # Update game state
    pygame.display.flip()
    clock.tick(60)