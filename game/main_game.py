import pygame
import sys
import random
from parameters import *
from background import *
from Bullet import Bullet, bullets
from Enemy import *

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arena")

#Main loop
running = True
background = screen.copy()
draw_bg(background)

#call enemy group
add_enemies(3)

lives = NUM_LIVES

while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet = Bullet(player.rect.x, player.rect.y, player.angle)
        bullets.add(bullet)

    #Allow sprite movements with their respective functions
    player.forward()
    player.rotate_right()
    player.rotate_left()
    enemies.update()     #Follows player
    bullets.update() #Creates bullet track

    # draw bg
    screen.blit(background, (0, 0))

    # draw player and enemies
    player.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    # update display
    pygame.display.flip()

#Exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()