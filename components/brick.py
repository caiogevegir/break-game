import pygame

class Brick(pygame.sprite.Sprite):
    
    width = 64
    height = 32
    num_images = 4

    vertical_offset = 48
    horizontal_offset = 4
    space_between_bricks = 4

    def __init__(self, image_path: str, i: int, j: int) -> None:
        super().__init__()
        self.image = Brick.__get_image(image_path, i)
        self.rect = self.image.get_rect()
        self.__spawn(i, j)

    @staticmethod
    def __get_image(image_path, i) -> pygame.Surface:
        return pygame.image.load(image_path).subsurface(
            [0, Brick.height * (i % Brick.num_images)], 
            [Brick.width, Brick.height]
        )
    
    def __spawn(self, i, j):
        self.rect.x, self.rect.y = (
            (Brick.horizontal_offset + j*(Brick.space_between_bricks + Brick.width)), 
            (Brick.vertical_offset + i*(Brick.space_between_bricks + Brick.height))
        )
