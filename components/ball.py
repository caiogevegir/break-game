import pygame

class Ball(pygame.sprite.Sprite):

    speed_increase_rate = 1.025
    spawn_point = (240, 360)
    starting_velocity = [2, 2]
    size = 16
    
    def __init__(self, image_path: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.velocity = Ball.starting_velocity
        self.spawn()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def speed_up(self):
        self.velocity[0] *= Ball.speed_increase_rate
        self.velocity[1] *= Ball.speed_increase_rate

    def bounce_vertical(self):
        self.velocity[1] *= -1
    
    def bounce_horizontal(self):
        self.velocity[0] *= -1
    
    def spawn(self):
        self.rect.x, self.rect.y = Ball.spawn_point
    
    def has_collided_with_paddle(self, paddle) -> bool:
        return pygame.sprite.collide_mask(self, paddle)
