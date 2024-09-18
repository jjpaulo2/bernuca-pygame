from typing import Any
from pygame.sprite import Sprite
from pygame.rect import Rect

from game.settings import SPRITES_PATH_BERNUCA


class BernucaSprite(Sprite):

    def __init__(self, width: float = 115.66, height: float = 26):
        super().__init__()
        self.starter_width = width
        self.starter_heigth = height
        self.velocity_x = 0
        self.velocity_y = 0
        self.x = 10
        self.y = 10
        self.size = 1
        self.images = [
            SPRITES_PATH_BERNUCA / 'legs-0.png',
            SPRITES_PATH_BERNUCA / 'legs-1.png',
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = Rect(self.x, self.y, self.starter_width, self.starter_heigth)

    def update(self, *args, **kwargs):
        if self.image_index == 0:
            self.image_index = 1
        else:
            self.image_index = 0
        
        self.image = self.images[self.image_index]
        