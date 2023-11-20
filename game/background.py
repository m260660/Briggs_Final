import pygame
from parameters import *

#define function for bg
def draw_bg(screen):
    #fill screen
    space = pygame.image.load("../assets/sprites/space.jpg").convert()
    for x in range(0,SCREEN_WIDTH, TILE_SIZE):
        for y in range(0,SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(space, (x,y))

    #add obstacles


