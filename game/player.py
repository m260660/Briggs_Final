import math
import time
import pygame
from parameters import *
from Bullet import *

#create pygame sprite class for a player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.angle = PLAYER_ANGLE
        self.image = pygame.image.load("../assets/sprites/player.png")
        self.up_image = pygame.transform.rotate(self.image, 0)
        self.rect = self.up_image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
        self.speed = PLAYER_SPEED

    def rotate_right(self):
        if abs(self.angle) > 360:
            self.angle = 0
        keys = pygame.key.get_pressed()  # returns a lst of keys
        if keys[pygame.K_RIGHT]:
            self.angle -= TURN_SPEED
            self.up_image = pygame.transform.rotate(self.image, self.angle)
            print(self.angle)

    def rotate_left(self):
        if abs(self.angle) > 360:
            self.angle = 0
        keys = pygame.key.get_pressed()  # returns a lst of keys
        if keys[pygame.K_LEFT]:
            self.angle += TURN_SPEED
            self.up_image = pygame.transform.rotate(self.image, self.angle)
            print(self.angle)

    def forward(self):
        dx = 0
        dy = 0
        speed = PLAYER_SPEED
        keys = pygame.key.get_pressed()  # returns a lst of keys
        rad_angle = math.radians(self.angle)  #Credits to CAPT Severson for degree conversion
        if keys[pygame.K_UP]: # Credits to Jackson Winner for the key functions
            # dx = math.cos(rad_angle) * self.speed
            # dy = math.sin(rad_angle) * self.speed

            if rad_angle > 90 or rad_angle < 270:
                dx += math.cos(rad_angle) * self.speed
            elif rad_angle < 90 or rad_angle > 270:
                dx += -math.cos(rad_angle) * self.speed
            if rad_angle > 0 or rad_angle < 180:
                dy += -math.sin(rad_angle) * self.speed
            elif rad_angle > 180 or rad_angle < 360:
                dy += math.sin(rad_angle) * self.speed

        self.x += dx
        self.y += dy



    def draw(self, screen):
        screen.blit(self.up_image, (self.x, self.y))

