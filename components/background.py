import pygame

class Background:
    
    default_position = (0, 0)
    
    def __init__(self, image_path) -> None:
        self.image = pygame.image.load(image_path)
    
    def draw(self, screen):
        screen.blit(self.image, Background.default_position)