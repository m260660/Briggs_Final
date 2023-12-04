import pygame
import sys
import random
from parameters import *
from background import *
from Bullet import Bullet, bullets
from Enemy_Bullet import Enemy_Bullet, enemy_bullets
from Enemy import *

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arena")

#Main loop
running = True
background = screen.copy()
draw_bg(background)

# call enemy group
add_enemies(10)

#uses player as life icon
life_icon = pygame.image.load("../assets/sprites/player.png").convert()

font = pygame.font.Font("../assets/fonts/space_font.otf", size=30)
lives = NUM_LIVES
score = 0

#sounds
player_shoot = pygame.mixer.Sound("../assets/sounds/player_shoot.wav")
player_hit = pygame.mixer.Sound("../assets/sounds/player_hit.wav")
enemy_shoot = pygame.mixer.Sound("../assets/sounds/enemy_shoot.wav")
enemy_hit = pygame.mixer.Sound("../assets/sounds/enemy_hit.wav")
theme = pygame.mixer.Sound("../assets/sounds/SWtheme.mp3") #background music

#play game over sound effect
pygame.mixer.Sound.play(theme)

while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet = Bullet(player.rect.x, player.rect.y, player.angle)
        bullets.add(bullet)
        pygame.mixer.Sound.play(player_shoot)

    if random.randint(1,350) == 1: #randomizes enemy bullets being fired
        for enemy in enemies:
            enemy_bullet = Enemy_Bullet(enemy.x, enemy.y, math.degrees(enemy.angle)) #references the instantaneous position of the enemy
            enemy_bullets.add(enemy_bullet)
            pygame.mixer.Sound.play(enemy_shoot)

    #Allow sprite movements with their respective functions
    player.forward()
    player.rotate_right()
    player.rotate_left()
    enemies.update()     #Follows player
    bullets.update() #Creates bullet track
    enemy_bullets.update()

    # draw bg
    screen.blit(background, (0, 0))

    #Check for player and enemy bullet collisions
    result = pygame.sprite.spritecollide(player, enemy_bullets, True)
    if result:
        # play hurt sound
        pygame.mixer.Sound.play(player_hit)
        lives -= 1

    # check for enemy and bullet collisions
    result = pygame.sprite.groupcollide(bullets, enemies, True, True)
    # credits to Mathew Robinson for helping configure groupcollide
    if result:
        # play hit sound
        pygame.mixer.Sound.play(enemy_hit)
        score += len(result)
        print(score)
        # draw more enemies on screen
        add_enemies(len(result))

    # draw player and enemies
    player.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    enemy_bullets.draw(screen)

    # draw the score on the screen
    text = font.render(f'score: {score}', True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH/2, 500)) #Catie Gajski helped with making the score visible after 2 digits

    # draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * 55, SCREEN_HEIGHT - TILE_SIZE))

    pygame.display.flip()

    # limit time frame
    # clock.tick(3600)

#once all lives are gone
#create new bg when game over
screen.blit(background,(0,0))

#show game over message and show final score
message = font.render("GAME OVER!",True, (255,255,255))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - message.get_height()/2))
score_text = font.render(f"Score: {score}", True, (0,255,0))
screen.blit(score_text, (SCREEN_WIDTH/2 -score_text.get_width()/2, SCREEN_HEIGHT/2 - 3*score_text.get_height()/2))

#update display
pygame.display.flip()

#Exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()