import pygame

class Brick(pygame.sprite.Sprite):
    
    def __init__(self, image, position) -> None:
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]