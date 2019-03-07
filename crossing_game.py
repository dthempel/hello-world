### cross the road

import pygame

# print(dir(pygame))

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Crossy RPG"
WHITE_COLOR = (255,255,255)  # RED, GREEN, BLUE
BLACK_COLOR = (0,0,0)

clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

game_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(640,480))

player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image,(50,50))

while not is_game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)

    game_screen.blit(background, (0,0))
    game_screen.blit(player_image, (295,430))

    pygame.display.update()
    clock.tick(TICK_RATE)

pygame.quit()
quit()
