import math
import time
import pygame
from parameters import *
from Bullet import *

#create pygame sprite class for a player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.angle = 0
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
        self.angle -= TURN_SPEED
        self.up_image = pygame.transform.rotate(self.image, self.angle)

    def rotate_left(self):
        self.angle += TURN_SPEED
        self.up_image = pygame.transform.rotate(self.image, self.angle)

    def forward(self):
        self.speed = PLAYER_SPEED
        self.x_speed += math.cos(self.angle) * self.speed
        self.y_speed += math.sin(self.angle) * self.speed

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.angle += ANGLE
        if self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH - TILE_SIZE
        if self.x < 0:
            self.x = 0
        if self.y > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.y = SCREEN_HEIGHT - 2 * TILE_SIZE
        if self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y
        print(self.angle)



    def draw(self, screen):
        screen.blit(self.up_image, (self.rect.x, self.rect.y))

