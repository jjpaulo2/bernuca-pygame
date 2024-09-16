import pygame
from game.settings import BACKGROUND_PATH, WINDOW_SIZE, WINDOW_TITLE, WINDOW_CLOCK
from game.sprite import BernucaSprite


def loop(window: pygame.Surface, clock: pygame.time.Clock):
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                break

        pygame.display.flip()
        background_image = pygame.image.load(BACKGROUND_PATH)
        window.blit(background_image, (0,0,))
        clock.tick(WINDOW_CLOCK)

    else:
        pygame.quit()

def main():
    pygame.mixer.pre_init(44100, 16, 2, 1024)
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    window = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group(BernucaSprite())
    sprites.draw(window)

    loop(window, clock)
