import pygame
from enum import Enum

class Ball(pygame.sprite.Sprite):
    
    class CollisionDirection(Enum):
        X=1,
        Y=2
    
    def __init__(self, image: pygame.image, position: list, velocity: list) -> None:
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def increase_speed(self, rate):
        self.velocity[0] *= rate
        self.velocity[1] *= rate
    
    def bounce(self, direction):
        match direction:
            case Ball.CollisionDirection.Y:
                self.velocity[1] *= -1
            case Ball.CollisionDirection.X:
                self.velocity[0] *= -1
    
    def has_collided_with_paddle(self, paddle):
        return pygame.sprite.collide_mask(self, paddle)
