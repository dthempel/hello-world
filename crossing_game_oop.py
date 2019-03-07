### cross the road

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Crossy RPG"
WHITE_COLOR = (255,255,255)  # RED, GREEN, BLUE
BLACK_COLOR = (0,0,0)

clock = pygame.time.Clock()

class Game:

    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width,height))
        self.game_screen.fill(WHITE_COLOR)

        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            #game_screen.blit(background, (0,0))
            #game_screen.blit(player_image, (295,430))

            pygame.display.update()
            clock.tick(self.TICK_RATE)

pygame.init()

new_game = Game("My Game", 640, 480)
new_game.run_game_loop()

#background = pygame.image.load('background.png')
#background = pygame.transform.scale(background,(640,480))

#player_image = pygame.image.load('player.png')
#player_image = pygame.transform.scale(player_image,(50,50))

pygame.quit()
quit()
