import pygame
from grid import *

# base settings
WIDTH = 1280
HEIGHT = 720
FPS = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# sprite groups
grid_sprites = pygame.sprite.Group()

# grid
grid_pos = (int(WIDTH/2), int(HEIGHT/2))
grid = Grid(grid_pos, 3, 3, 3, 3, grid_sprites)

# custom events
FULLSCREEN = pygame.USEREVENT + 1

while running:
    for event in pygame.event.get():

        # Checks for keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_f:
                pygame.event.post(pygame.event.Event(FULLSCREEN))

        # Checks for quit
        elif event.type == pygame.QUIT:
            running = False

        # Checks for fullscreen event
        elif event.type == FULLSCREEN:
            if screen.get_flags() & pygame.FULLSCREEN:
                pygame.display.set_mode((WIDTH, HEIGHT))
            else:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # CGPT

    screen.fill("white")

    # RENDER YOUR GAME HERE
    grid_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()
