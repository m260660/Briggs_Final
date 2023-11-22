import pygame
import sys
from parameters import *
from background import *
from player import *
from Bullet import *

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arena")

#create a player
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
bullet = Projectile(0,0, player.angle)

#Main loop
running = True
background = screen.copy()
draw_bg(background)

lives = NUM_LIVES

bullets = []
while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control player with keyboard
        player.stop()
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_DOWN:
            #     print("you pressed da down key")
            #     player.move_down()
            if event.key == pygame.K_UP:
                print("you pressed da up key")
                player.forward()
            if event.key == pygame.K_LEFT:
                print("you pressed da left key")
                player.rotate_left()
            if event.key == pygame.K_RIGHT:
                print("you pressed da rite key")
                player.rotate_right()
            if event.key == pygame.K_SPACE:
                # round = screen.  blit(background, (player.x, player.y))
                round = bullet.draw(screen)
                bullet.update()
                bullets.append(round)
                print("yay")
    for round in bullets:
        if bullet.x < 1000 and bullet.x > 0 and bullet.y > 0 and bullet.y < 600:
            bullet.x += BULLET_SPEED
            bullet.y += BULLET_SPEED
        else:
            bullets.remove(round)


    player.update()
    # bullet.update()

    #draw bg
    screen.blit(background, (0,0))

    #draw player and enemies
    player.draw(screen)


    # update display
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
