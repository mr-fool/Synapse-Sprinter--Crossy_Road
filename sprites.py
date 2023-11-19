
import pygame
import random


# List of character URLs
cars =["images/car.png", "images/car_2.png", "images/car_3.png"]
playerpic=["images/player.png", "images/player_2.png", "images/player_3.png", "images/player_4.png", "images/player_5.png", "images/player_1.png"]
tree = ["images/tree.png", "images/log.png"]


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, w, h)
        playerrandom = random.choices(playerpic)
        image = pygame.image.load(playerrandom[0])
        self.image_ract = self.rect
        self.resized_image = pygame.transform.scale(image, (w*3, h*3))
        self.color = (0, 128, 255)
        self.lives = 3

    def move_x(self, amount):
        self.x += amount
    
    def move_y(self, amount):
        self.y += amount

    def update(self, cam_x, cam_y):
        self.rect.x = self.x + cam_x
        self.rect.y = self.y + cam_y

    def collides_with(self, enemy):
        buffer = 1
        return self.rect.x+self.rect.w-buffer > enemy.rect.x and self.rect.x+buffer < enemy.rect.x+enemy.rect.w and self.rect.y+self.rect.h-buffer > enemy.rect.y and self.rect.y+buffer < enemy.rect.y+enemy.rect.h
    
    def out_of_bounds(self, screen_width, screen_height):
        return self.rect.x+self.rect.w < 0 or self.rect.x > screen_width or self.rect.y+self.rect.h < 0 or self.rect.y > screen_height
    
    def draw(self, screen):
        screen.blit(self.resized_image, self.image_ract)

class Enemy:
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.speed = speed
        self.color = (255, 0, 0)
        carsrandom = random.choices(cars)
        self.image = pygame.image.load(carsrandom[0])
        self.image_rect = self.rect
        self.resized_image = pygame.transform.scale(self.image, (w*3, h*3))
        if self.speed == 0:
            treerandom = random.choices(tree)
            self.image = pygame.image.load(treerandom[0])
            self.image_rect = self.rect
            self.resized_image = pygame.transform.scale(self.image, (w*3, h*3))

    def update(self, cam_x, cam_y):
        self.rect.x = self.x + cam_x
        self.rect.y = self.y + cam_y
    
    def draw(self, screen):
         screen.blit(self.resized_image, self.image_rect)
    
    def move(self):
        self.x += self.speed
    
    def flip(self, direction):
        if direction == 1:
            self.resized_image = pygame.transform.flip(self.resized_image, True, False)
    
    def off_screen(self, screen_height):
        return self.rect.y > screen_height+100
    
