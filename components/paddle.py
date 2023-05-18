import pygame

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, image: pygame.image, position: list) -> None:
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def move_left(self, unit, left_limit):
        self.rect.x -= unit
        if self.rect.x < left_limit:
          self.rect.x = left_limit
    
    def move_right(self, unit, right_limit):
        self.rect.x += unit
        if self.rect.x > right_limit:
          self.rect.x = right_limit
