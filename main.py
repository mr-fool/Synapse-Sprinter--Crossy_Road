import sys
import pygame
import random
import sprites
import serial
import threading
import time


# Dev testing
ARDUINO_MODE = False

ser = ''
if ARDUINO_MODE:
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

if ARDUINO_MODE:
    arduino_data_thread = threading.Thread(target=arduino_data, daemon=True)
    arduino_data_thread.start()

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arduino Crossy Road")

# Primary colours
background_img = pygame.image.load("images/background.png")
background_img_rect_1 = background_img.get_rect()
background_img_rect_2 = background_img.get_rect()
background_y = 0


# Basic colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Camera
cam_x = 0
cam_y = 0

game_score = 0
score_counter = 0
# Player setup
player_1 = sprites.Player(WIDTH//2-100, HEIGHT//2, 25, 25)
player_2 = sprites.Player(WIDTH//2+100, HEIGHT//2, 25, 25)

# Player setup
player_1 = sprites.Player(WIDTH//2-100, HEIGHT//2, 25, 25)
player_2 = sprites.Player(WIDTH//2+100, HEIGHT//2, 25, 25)
# Enemy setup
enemies = []
clock = pygame.time.Clock()

bg_music = pygame.mixer.music.load("sounds/game_music.wav")
pygame.mixer.music.play(-1)

hit_sound = pygame.mixer.Sound("sounds/game_over.wav")

def exit_code():
    print('='*24)
    print("Quitting py game")
    if ARDUINO_MODE:
        ser.close()
    print("closing serial connection")
    print("Exiting...")
    sys.exit()


def end_game():
    print('='*24)
    pygame.mixer.music.load("sounds/winner.wav")
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
        # Exit game
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                if player_1.lives > 0:
                    print("PLAYER ONE WON!")
                else:
                    print("PLAYER TWO WON!")
                print("Game score: ", game_score)
                pygame.quit()
                exit_code()

        screen.fill(BLACK)
        string = f"WINNER: {1 if player_1.lives > 0 else 2} SCORE: {game_score}"
        end_text = pygame.font.SysFont("Arial", 50).render(string, True, WHITE)
        text_rect = end_text.get_rect(center=(WIDTH//2, HEIGHT//2-50))
        screen.blit(end_text, text_rect)
        pygame.display.flip()

    

while True:
    #print(f"left: {sig1}, right: {sig2}")
    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit_code()
            
        # Keydown events

        elif event.type == pygame.KEYDOWN and not ARDUINO_MODE:
            if event.key == pygame.K_UP:
                player_1.move_y(-25)
            if event.key == pygame.K_LEFT:
                player_1.move_x(-25)
            if event.key == pygame.K_RIGHT:
                player_1.move_x(25)
            if event.key == pygame.K_w:
                player_2.move_y(-25)
            if event.key == pygame.K_a:
                player_2.move_x(-25)
            if event.key == pygame.K_d:
                player_2.move_x(25)

               
    if ARDUINO_MODE:
      player_speed = 25
      if cam_y%10 == 0:
          if sig1 > 0 and sig2 > 0:
              print("forward")
              player_1.move_y(-player_speed)
          elif sig1 > 0:
              print("left")
              player_1.move_x(-player_speed)
          elif sig2 > 0:
              print("right")
              player_1.move_x(player_speed)

    
    # Camera control
    cam_y += 1

    # Set background
    background_img_rect_1.y = background_y + cam_y%HEIGHT
    background_img_rect_2.y = background_y - HEIGHT + cam_y%HEIGHT
    screen.blit(background_img, background_img_rect_1)
    screen.blit(background_img, background_img_rect_2)
    



    score_counter += 1
    if score_counter%10 == 0:
        game_score += 1

    # Spawn enemies
    enemy_spawn_rate = 1
    enemy_count_limit = 25  # Match with the camera y to align it to a grid and prevent weird overlap
    for i in range(random.randint(1, enemy_spawn_rate)):
        if cam_y%enemy_count_limit == 0:
            rand_dir = random.randint(0, 1)
            size = enemy_count_limit
            x = -50
            if rand_dir == 1:
                x = WIDTH+50
            # Align y to a grid
            grid_height = enemy_count_limit
            grid_height_count = HEIGHT/grid_height
            y = random.randint(0, int(round(grid_height_count))) * int(round(grid_height)) - int(round(cam_y))
            speed = random.randint(1, 5)
            if rand_dir == 1:
                speed *= -1
            enemy = sprites.Enemy(x, y, size, size, speed)
            enemy.flip(rand_dir)
            enemies.append(enemy)
    
    
    # Update all enemies
    for enemy in enemies:
        enemy.move()
        enemy.update(cam_x, cam_y)
        enemy.draw(screen)

        if enemy.off_screen(HEIGHT):
            enemies.remove(enemy)
        # Check collision between players and enemies
        if player_1.collides_with(enemy):
            hit_sound.play()
            player_1.lives -= 1
            enemies.remove(enemy)
        if player_2.collides_with(enemy):
            hit_sound.play()
            player_2.lives -= 1
            enemies.remove(enemy)

    # Update all players (2)
    player_1.update(cam_x, cam_y)
    player_2.update(cam_x, cam_y)
    player_1.draw(screen)
    player_2.draw(screen)
    
    if player_1.out_of_bounds(WIDTH, HEIGHT):
        player_1.lives = 0
    if player_2.out_of_bounds(WIDTH, HEIGHT):
        player_2.lives = 0

    #print(player_1.lives, player_2.lives)
    if player_1.lives == 0 or player_2.lives == 0:
        pygame.mixer.music.stop()
        end_game()

    print("P1: "+str(player_1.lives) + "  P2: "+str(player_2.lives) + "  score: "+str(game_score))

    # Update game state
    pygame.display.flip()
    clock.tick(60)
