import pygame
import random
from parameters import *
from player import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/enemy.png")
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED,MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    

enemies = pygame.sprite.Group()

def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*1.5), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))