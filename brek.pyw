import pygame
import os.path
import sys

from components.background import Background
from components.statusbar import StatusBar
from components.paddle import Paddle
from components.ball import Ball
from components.brick import Brick

BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')
CONTENT_PATH = {
    'background': os.path.join(ASSETS_PATH, 'bg.png'),
    'paddle': os.path.join(ASSETS_PATH, 'paddle.png'),
    'ball': os.path.join(ASSETS_PATH, 'ball.png'),
    'bricks': os.path.join(ASSETS_PATH, 'bricks.png')
}

# Game Setup ---------------------------------------------------------------------------------------

WIDTH, HEIGHT = (480, 640)
FPS = 60
BRICK_ROWS, BRICK_COLUMNS = (8, 7)

score = 0
lives = 3

pygame.init()
pygame.display.set_caption('Brek')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
StatusBar.initialize_font()
clock = pygame.time.Clock()
sprites_list = pygame.sprite.Group()
bricks_list = pygame.sprite.Group()

background = Background(CONTENT_PATH['background'])
paddle = Paddle(CONTENT_PATH['paddle'])
ball = Ball(CONTENT_PATH['ball'])
for i in range(BRICK_ROWS):
    for j in range(BRICK_COLUMNS):
        brick = Brick(CONTENT_PATH['bricks'], i, j)
        bricks_list.add(brick)
        sprites_list.add(brick)
sprites_list.add(paddle)
sprites_list.add(ball)

# Game Methods -------------------------------------------------------------------------------------

def process_game_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()
    if keys[pygame.K_RIGHT]:
        paddle.move_right()


def process_game_logic():
    global lives, score
    sprites_list.update()
    if ball.rect.x <= 0 or ball.rect.x >= WIDTH-Ball.size:
        ball.bounce_horizontal()
    elif ball.rect.y <= 0 or ball.has_collided_with_paddle(paddle):
        ball.bounce_vertical()
    elif ball.rect.y >= HEIGHT:
        # Player missed the ball
        pygame.time.wait(1000)
        lives -= 1
        ball.spawn()
        paddle.spawn()
        return

    brick_collision_list = pygame.sprite.spritecollide(ball, bricks_list, False)
    for brick in brick_collision_list:
        brick.kill()
        ball.bounce_vertical()
        score += 10
        ball.speed_up()


def draw_content_on_screen():
    background.draw(screen)
    sprites_list.draw(screen)
    StatusBar.display_score(screen, score)
    StatusBar.display_lives(screen, lives)


def check_game_state() -> bool:
    # Win condition
    if len(bricks_list) == 0:
        StatusBar.display_win_message(screen)
        return False
    # Loss condition
    if lives < 1:
        StatusBar.display_loss_message(screen)
        return False
    # Keep gaming
    return True

# Main Loop ----------------------------------------------------------------------------------------

def main():
    running = True
    while running:
        process_game_events()
        process_game_logic()
        draw_content_on_screen()
        running = check_game_state()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
