### cross the road

import pygame

SCREEN_TITLE = "Crossy RPG"
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
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
        direction = 0
        player_size = 50
        enemy_size = 50

        player_character = PlayerCharacter('player.png', 320, 430, player_size, player_size)
        enemy_character0 = EnemyCharacter('enemy.png', 320, 230, enemy_size, enemy_size)

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

                print(event)

            #game_screen.blit(background, (0,0))
            #game_screen.blit(player_image, (295,430))

            self.game_screen.fill(WHITE_COLOR)

            player_character.move(direction, self.height, player_size)
            player_character.draw(self.game_screen)

            enemy_character0.move(self.width, enemy_size)
            enemy_character0.draw(self.game_screen)

            pygame.display.update()
            clock.tick(self.TICK_RATE)

class GameObject:

    def __init__(self, image_path, x, y, width, height):

        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image,(width,height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height
    
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height, player_size):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - player_size:
            self.y_pos = max_height - player_size

        if self.y_pos <= 0:
            self.y_pos = 0
       


class EnemyCharacter(GameObject):

    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width, size):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - (20 + size):
            self.SPEED = -abs(self.SPEED)
        
        self.x_pos += self.SPEED
        


pygame.init()

new_game = Game("My Game", 640, 480)
new_game.run_game_loop()

#background = pygame.image.load('background.png')
#background = pygame.transform.scale(background,(640,480))

pygame.quit()
quit()
