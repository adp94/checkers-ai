import pygame

# dimensions
HEIGHT, WIDTH = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (32, 32, 255) 
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/crown.png'), (44,25))