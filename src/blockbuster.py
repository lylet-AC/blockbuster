import pygame
import random
import os

WIDTH = 480  # width of our game window
HEIGHT = 600 # height of our game window
FPS = 30 # frames per second

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
sprite_folder = os.path.join(game_folder, 'sprites')

pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw / render
    screen.fill(0, 0, 0)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
