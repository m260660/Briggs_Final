from parameters import *

#define function for bg
def draw_bg(screen):
    #fill screen
    space = pygame.image.load("../assets/sprites/space.jpg").convert()
    for x in range(0,SCREEN_WIDTH, TILE_SIZE):
        for y in range(0,SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(space, (x,y))

    # draw text
    font = pygame.font.Font("../assets/fonts/space_font.otf", size=45)
    text = font.render('LightSpeed', True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, text.get_height() / 4))
