import pygame

WINDOW_SIZE = (800, 600)
WINDOW_TITLE = 'Bernuça Game'
STARTER_POSITION = (10, 10)


pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)


window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            print('Fechando...')

    pygame.display.flip()
    clock.tick(30)


pygame.quit()