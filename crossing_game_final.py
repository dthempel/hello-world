### cross the field

import pygame

#WHITE_COLOR = (255,255,255)  # RED, GREEN, BLUE
BLACK_COLOR = (0,0,0)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('calibri', 75)

class Game:

    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width,height))
        #self.game_screen.fill(WHITE_COLOR)

        pygame.display.set_caption(title)

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0
        player_size = 50
        enemy_size = 50

        player_character = PlayerCharacter('player.png', 295, 430, player_size, player_size)
        enemy_character0 = EnemyCharacter('enemy.png', 200, 130, enemy_size, enemy_size)
        enemy_character1 = EnemyCharacter('enemy.png', 400, 330, enemy_size, enemy_size)
        treasure = GameObject('treasure.png', 295, 1, 50, 50)
        background = GameObject('background.png', 0, 0, 640, 480)

        enemy_character0.SPEED *= level_speed
        enemy_character1.SPEED *= level_speed

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

            ##self.game_screen.fill(WHITE_COLOR)

            background.draw(self.game_screen)

            treasure.draw(self.game_screen)

            player_character.move(direction, self.height, player_size)
            player_character.draw(self.game_screen)

            enemy_character0.move(self.width, enemy_size)
            enemy_character0.draw(self.game_screen)

            enemy_character1.move(self.width, enemy_size)
            enemy_character1.draw(self.game_screen)

            if player_character.detect_collision(enemy_character0):
                is_game_over = True
                did_win = False
                text = font.render('You\'ve Lost!', True, BLACK_COLOR)
                self.game_screen.blit(text, (100,200))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(enemy_character1):
                is_game_over = True
                did_win = False
                text = font.render('You\'ve Lost!', True, BLACK_COLOR)
                self.game_screen.blit(text, (100,200))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You\'ve Won!', True, BLACK_COLOR)
                self.game_screen.blit(text, (100,200))
                pygame.display.update()
                clock.tick(1)
                break

            pygame.display.update()
            clock.tick(self.TICK_RATE)
        
        if did_win:
            self.run_game_loop(level_speed + 0.25)
        else:
            return

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
    
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True

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
new_game.run_game_loop(1)

pygame.quit()
quit()
