import pygame
from constants import SPEED, WIDTH, HEIGHT

def get_screen(width, height):
    return pygame.display.set_mode((width, height))

def get_x(i, x):
    return (i + x * SPEED) % WIDTH


def get_y(j, y):
    return (j + y * SPEED) % HEIGHT

