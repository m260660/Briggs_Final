import math
import pygame
from parameters import *

class Projectile(pygame.sprite.Sprite): #creating class for bullet
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/bullet.png") #loading image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = x
        self.rect.center = (x, y)
        self.angle = angle

    def update(self):
        self.x += math.cos(self.angle) + BULLET_SPEED #updates speed of bullet based on direction
        self.y += math.sin(self.angle) + BULLET_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))








