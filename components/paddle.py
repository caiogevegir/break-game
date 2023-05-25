import pygame

class Paddle(pygame.sprite.Sprite):

    width = 96
    spawn_point = (192, 560) # screen_width/2 - paddle_width/2
    movement_unit = 16
    left_limit = 0
    right_limit = 384        # screen_width - paddle_width
    
    def __init__(self, image_path: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.spawn()

    def move_left(self):
        self.rect.x -= Paddle.movement_unit
        if self.rect.x < Paddle.left_limit:
            self.rect.x = Paddle.left_limit
    
    def move_right(self):
        self.rect.x += Paddle.movement_unit
        if self.rect.x > Paddle.right_limit:
            self.rect.x = Paddle.right_limit
    
    def spawn(self):
       self.rect.x, self.rect.y = Paddle.spawn_point
