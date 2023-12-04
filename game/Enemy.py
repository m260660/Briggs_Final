import math
import pygame
import random
from parameters import *
from player import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        super().__init__()
        self.angle = ENEMY_ANGLE
        self.image = pygame.image.load("../assets/sprites/enemy.png")
        self.up_image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.center = (self.x, self.y)
        self.speed = ENEMY_SPEED

    def update(self):
        dx = player.x - self.rect.x #credit to Jackson Winner for finding a correct way to import x and y from Player :)
        dy = player.y - self.rect.y

        distance = math.hypot(dx, dy)
        dx = dx / (distance + 0.00001)
        dy = dy / (distance + 0.00001)

        # add cond for distance
        self.x += dx * self.speed
        self.y += dy * self.speed

        self.angle = math.atan2(dy, dx) #TROUBLE
        # self.angle = math.degrees(self.angle)
        if dx >= 0:
            self.angle -= TURN_SPEED
            if abs(self.angle) > 360:
                self.angle = 0
        if dx < 0:
            self.angle += TURN_SPEED
            if abs(self.angle) > 360:
                self.angle = 0

        rad_angle = math.radians(self.angle)

        self.up_image = pygame.transform.rotate(self.image, rad_angle)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.up_image, (self.x, self.y))

enemies = pygame.sprite.Group()
# enemy = Enemy(SCREEN_WIDTH/3, SCREEN_HEIGHT/3)

def add_enemies(num_enemies):
    for _ in range(num_enemies):
        # enemies.add(Enemy(random.randint(SCREEN_WIDTH/2, SCREEN_WIDTH), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*1.5), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))