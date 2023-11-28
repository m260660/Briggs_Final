import math
import time
import pygame
from parameters import *
from Bullet import *

# keys = pygame.key.get_pressed() #returns a lst of keys

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
        if keys[pygame.K_UP]:
            if self.angle > 90 or self.angle < 270:
                dx += math.cos(self.angle) * self.speed
            elif self.angle < 90 or self.angle > 270:
                dx += -math.cos(self.angle) * self.speed
            if self.angle > 0 or self.angle < 180:
                dy += -math.sin(self.angle) * self.speed
            elif self.angle > 180 or self.angle < 360:
                dy += math.sin(self.angle) * self.speed

            # if self.angle < -90 or self.angle > -270:
            #     dx += -math.cos(self.angle) * self.speed
            # elif self.angle > -90 or self.angle < -270:
            #     dx += math.cos(self.angle) * self.speed
            # if self.angle < 0 or self.angle > -180:
            #     dy += math.sin(self.angle) * self.speed
            # elif self.angle < -180 or self.angle > -360:
            #     dy += -math.sin(self.angle) * self.speed

            # if self.angle > 90 or self.angle < 270 or self.angle > -90 or self.angle < -270:
            #     dx += -math.cos(self.angle) * self.speed
            # elif self.angle < 90 or self.angle > 270 or self.angle < -90 or self.angle > -270:
            #     dx += math.cos(self.angle) * self.speed
            # if self.angle > 0 or self.angle < 180 or self.angle < -180 or self.angle > -360:
            #     dy += -math.sin(self.angle) * self.speed
            # elif self.angle > 180 or self.angle < 360 or self.angle < 0 or self.angle > -180:
            #     dy += math.sin(self.angle) * self.speed

            # dx *= (1/math.sqrt(2))
            # dy *= (1/math.sqrt(2))

        self.x += dx
        self.y += dy



    def draw(self, screen):
        screen.blit(self.up_image, (self.x, self.y))

