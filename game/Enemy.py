import pygame
import random
from parameters import *
from player import *

player_x = Player.x
player_y = Player.y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.angle = ENEMY_ANGLE
        self.image = pygame.image.load("../assets/sprites/enemy.png")
        self.up_image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
        self.speed = ENEMY_SPEED




    def update(self):
        dx = 0
        dy = 0

        distance_x = player_x - self.x
        distance_y = player_y - self.y
        if abs(distance_x) < 50 or abs(distance_y) < 50:
            self.speed = PLAYER_SPEED
        if abs(distance_x) > 50 or abs(distance_y) > 50:
            self.speed = ENEMY_SPEED

        self.angle = math.atan2(distance_y, distance_x)
        if abs(self.angle) > 360:
            self.angle = 0

        rad_angle = math.radians(self.angle)
        self.up_image = pygame.transform.rotate(self.image, self.angle)

        self.x -= distance_x
        self.y -= distance_y

    def draw(self, screen):
        screen.blit(self.up_image, (self.x, self.y))

# enemies = pygame.sprite.Group()

    # def add_enemies(num_enemies):
    #     for _ in range(num_enemies):
    #         enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*1.5), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))