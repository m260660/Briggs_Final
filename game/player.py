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
        keys = pygame.key.get_pressed()  # returns a lst of keys
        if keys[pygame.K_RIGHT]:
            self.angle -= TURN_SPEED
            self.up_image = pygame.transform.rotate(self.image, self.angle)

    def rotate_left(self):
        keys = pygame.key.get_pressed()  # returns a lst of keys
        if keys[pygame.K_LEFT]:
            self.angle += TURN_SPEED
            self.up_image = pygame.transform.rotate(self.image, self.angle)

    def forward(self):
        dx = 0
        dy = 0
        speed = PLAYER_SPEED
        keys = pygame.key.get_pressed() #returns a lst of keys
        if keys[pygame.K_UP]:
            dx += math.cos(self.angle) * self.speed
            dy += math.sin(self.angle) * self.speed

        self.x += dx
        self.y += dy

    #
    # def stop(self):
    #     self.x_speed = 0
    #     self.y_speed = 0

    # def update(self):
    #     # self.x += self.x_speed
    #     # self.y += self.y_speed
    #     self.angle += PLAYER_ANGLE
    #     if self.x > SCREEN_WIDTH - TILE_SIZE:
    #         self.x = SCREEN_WIDTH - TILE_SIZE
    #     if self.x < 0:
    #         self.x = 0
    #     if self.y > SCREEN_HEIGHT - 2 * TILE_SIZE:
    #         self.y = SCREEN_HEIGHT - 2 * TILE_SIZE
    #     if self.y < 0:
    #         self.y = 0
    #     self.rect.x = self.x
    #     self.rect.y = self.y
    #     print(self.angle)



    def draw(self, screen):
        screen.blit(self.up_image, (self.x, self.y))

