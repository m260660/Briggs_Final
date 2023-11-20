import math

import pygame
from parameters import *

#create pygame sprite class for a player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/player.png")
        self.up_image = pygame.transform.flip(self.image, False, False)
        self.down_image = pygame.transform.flip(self.image, True, True)
        self.right_image = pygame.transform.rotate(self.image, 270)
        self.left_image = pygame.transform.rotate(self.image, 90)
        self.nw_image = pygame.transform.rotate(self.image, 45)
        self.sw_image = pygame.transform.rotate(self.image, 135)
        self.nw_image = pygame.transform.rotate(self.image, 45)
        self.image = self.up_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED
        self.image = self.up_image

    def move_down(self):
        self.y_speed = PLAYER_SPEED
        self.image = self.down_image

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        self.image = self.left_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.right_image



    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):

        x_pos, y_pos = pygame.mouse.get_pos()
        dx = x_pos - self.rect.x
        dy = y_pos - self.rect.y

        distance = math.hypot(dx, dy)

        dx = dx / distance
        dy = dy / distance

        self.rect.x += dx * PLAYER_SPEED
        self.rect.y += dy * PLAYER_SPEED

        print(pygame.mouse.get_pos())
        print(self.rect.x, self.rect.y)
        #self.x += self.x_speed
        #self.y += self.y_speed
        #if self.x > SCREEN_WIDTH - TILE_SIZE:
        #    self.x = SCREEN_WIDTH - TILE_SIZE
        #if self.x < 0:
        #    self.x = 0
        #if self.y > SCREEN_HEIGHT - 2 * TILE_SIZE:
        #    self.y = SCREEN_HEIGHT - 2 * TILE_SIZE
        #if self.y < 0:
        #    self.y = 0
        #self.rect.x = self.x
        #self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

