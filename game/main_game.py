import pygame
import sys
import random
from parameters import *
from background import *
from player import *
from Bullet import *
from Enemy import *
import time

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arena")

#create a player
# player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
# enemy = Enemy(SCREEN_WIDTH/3, SCREEN_HEIGHT/3)

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

    player.forward()
    player.rotate_right()
    player.rotate_left()
    enemies.update()

    # player.update()
    bullets.update()

    # draw bg
    screen.blit(background, (0, 0))

    # for enemy in enemies:
    #     if enemy.rect.x < SCREEN_WIDTH or enemy.rect.y > SCREEN_WIDTH:
    #         enemies.remove(enemy)  # remove fish from sprite group
    #         add_enemies(1)


    # draw player and enemies
    player.draw(screen)
    enemies.draw(screen)

    # update display
    pygame.display.flip()

#Bullets

def shoot(self):
    keys = pygame.key.get_pressed()  # returns a lst of keys
    if keys[pygame.K_SPACE]:
        round = Bullet(0,0, player.angle)
        round = bullets.update()
        # bullet.update()
        bullets.add(round)
        print("yay")

# for bullet in bullets:
#     if bullet.x < 1000 and bullet.x > 0 and bullet.y > 0 and bullet.y < 600:
#         bullet.x += BULLET_SPEED
#         bullet.y += BULLET_SPEED
#     # detect for collisions
#     if bullet.x == enemies.x and bullet.y == enemies.y:
#         enemies.remove(1)
#         bullets.remove(1)
#     else:
#         bullets.remove(1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()