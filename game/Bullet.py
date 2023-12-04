import math
import pygame
from parameters import *

class Bullet(pygame.sprite.Sprite): #creating class for bullet
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/bullet.png") #loading image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.angle = angle

    def update(self):
        self.x += BULLET_SPEED * math.cos(math.radians(self.angle)) #updates speed of bullet based on direction
        self.y -= BULLET_SPEED * math.sin(math.radians(self.angle))
        if self.y < 0 or self.x < 0 or self.x > SCREEN_WIDTH:
            self.kill()

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.draw(self.image, self.rect)

bullets = pygame.sprite.Group()









