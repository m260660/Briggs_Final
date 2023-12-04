import math
import pygame
from parameters import *
from Bullet import Bullet, bullets

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

    def rotate_left(self):
        if abs(self.angle) > 360:
            self.angle = 0
        keys = pygame.key.get_pressed()  # returns a lst of keys
        if keys[pygame.K_LEFT]:
            self.angle += TURN_SPEED
            self.up_image = pygame.transform.rotate(self.image, self.angle)

    def forward(self):
        dx = 0
        dy = 0
        #speed = PLAYER_SPEED
        keys = pygame.key.get_pressed()  # returns a list of keys
        rad_angle = math.radians(self.angle)  #Credits to CAPT Severson for degree conversion
        if keys[pygame.K_UP]: # Credits to Jackson Winner for the key functions

            if abs(rad_angle) > 1.57 or abs(rad_angle) < 4.71:
                dx += math.cos(rad_angle) * self.speed
            elif abs(rad_angle) < 1.57 or abs(rad_angle) > 4.71:
                dx += -math.cos(rad_angle) * self.speed
            if abs(rad_angle) > 0 or abs(rad_angle) < 3.14:
                dy += -math.sin(rad_angle) * self.speed
            elif abs(rad_angle) > 3.14 or abs(rad_angle) < 6.28:
                dy += math.sin(rad_angle) * self.speed

        if self.x > SCREEN_WIDTH - TILE_SIZE: #Limits player movement to the screen dimensions
            self.x = SCREEN_WIDTH - TILE_SIZE
        if self.x < 0:
            self.x = 0
        if self.y > SCREEN_HEIGHT - 2*TILE_SIZE:
            self.y = SCREEN_HEIGHT - 2*TILE_SIZE
        if self.y < 0:
            self.y = 0

        self.x += dx
        self.y += dy

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.up_image, (self.x, self.y))

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
