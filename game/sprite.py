from pygame.sprite import Sprite
from pygame.rect import Rect

from game.settings import SPRITES_PATH_BERNUCA


class BernucaSprite(Sprite):

    def __init__(self, width: float = 115.66, height: float = 26):
        super().__init__()
        self.starter_width = width
        self.starter_heigth = height
        self.size = 1
        self.images = [
            SPRITES_PATH_BERNUCA / 'legs-0.png',
            SPRITES_PATH_BERNUCA / 'legs-1.png',
        ]
        self.image = self.images[0]
        self.rect = Rect(10, 10, self.starter_width, self.starter_heigth)
