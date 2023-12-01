import math
import pygame
from parameters import *
from player import player

player_x = player.x
player_y = player.y

class Bullet(pygame.sprite.Sprite): #creating class for bullet
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/bullet.png") #loading image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = x
        self.rect.center = (x, y)

    def update(self):
        dx = player.dx
        dy = player.dy
        distance = math.hypot(dx, dy)

        dx = dx / (distance)
        dy = dy / (distance)

        self.x += dx + BULLET_SPEED #updates speed of bullet based on direction
        self.y += dy + BULLET_SPEED

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.draw(self.image, (player_x, player_y))

bullets = pygame.sprite.Group()

# def add_bullets(num_bullets):
#     for _ in range(num_bullets):
#         bullets.add(Bullet(self.x, y)

def shoot(self):
    keys = pygame.key.get_pressed()  # returns a lst of keys
    if keys[pygame.K_SPACE]:
        round = Bullet(0,0)
        round = bullets.update()
        # bullet.update()
        bullets.add(round)
        print("yay")









