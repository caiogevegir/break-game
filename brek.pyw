import pygame
import os.path
import sys

from components.paddle import Paddle
from components.ball import Ball
from components.brick import Brick

BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')

WIDTH, HEIGHT, UNIT = 480, 640, 16
FPS = 60
SPEED_INCREASE_RATE = 1.025

score = 0
lives = 3

pygame.init()
pygame.display.set_caption('Brek')
running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('courier', 30)
sprites_list = pygame.sprite.Group()
bricks_list = pygame.sprite.Group()

background = pygame.image.load(os.path.join(ASSETS_PATH, 'bg.png'))
paddle = Paddle(
    image=pygame.image.load(os.path.join(ASSETS_PATH, 'paddle.png')),
    position=[240,560]
)
ball = Ball(
    image=pygame.image.load(os.path.join(ASSETS_PATH, 'ball.png')),
    position=[240,400],
    velocity=[2,2]
)

sprites_list.add(paddle)
sprites_list.add(ball)

for i in range(8):
    for j in range(7):
        brick = Brick(
            image=pygame.image.load(os.path.join(ASSETS_PATH, 'bricks.png')).subsurface([0,32*(i%4)], [64,32]),
            position=[(4 + 68*j),(48 + 36*i)]
        )
        sprites_list.add(brick)
        bricks_list.add(brick)

# Game Loop
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        paddle.move_left(UNIT, 0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        paddle.move_right(UNIT, WIDTH-96)

    # Logic
    sprites_list.update()
    if ball.rect.x <= 0 or ball.rect.x >= WIDTH-16:
        ball.bounce(Ball.CollisionDirection.X)
    if ball.rect.y <= 0 or ball.has_collided_with_paddle(paddle):
        ball.bounce(Ball.CollisionDirection.Y)
    if ball.rect.y >= HEIGHT:
        # Lose 1 life and restart
        lives -= 1
        ball.rect.x, ball.rect.y = 240, 400 

    brick_collision_list = pygame.sprite.spritecollide(ball, bricks_list, False)
    for brick in brick_collision_list:
        brick.kill()
        ball.bounce(Ball.CollisionDirection.Y)
        score += 10
        ball.increase_speed(SPEED_INCREASE_RATE)

    # Drawing
    screen.blit(background, [0,0])
    sprites_list.draw(screen)
    if len(bricks_list) == 0:
        # Game Win
        screen.blit(font.render('Ganhou! :)', True, (255,255,255)), [240,4])
        running = False
    elif lives < 0:
        # Game Over
        screen.blit(font.render('Game Over! :(', True, (255,255,255)), [240,4])
        running = False
    else:
        screen.blit(font.render(f'{score}', True, (255,255,255)), [4,4])
        screen.blit(font.render(f'\u2665 {lives}', True, (255,255,255)), [420, 4])
    
    # Update screen
    pygame.display.flip()
    # Framerate
    clock.tick(FPS)

pygame.time.wait(5000)
pygame.quit()
sys.exit()
