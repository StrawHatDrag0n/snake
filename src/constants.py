import pygame
from enum import Enum
import random

WIDTH = 800
HEIGHT = 800

CELL_SIZE = 10
SPEED = 10

FPS = 30

class GameState(Enum):
    START = 'start'
    PLAYING = 'playing'
    END = 'end'
class Fonts(Enum):
    comic_sans = 'Comic Sans MS'

class Text(Enum):
    score_text = 'Score: {}'
    game_over_text = 'GAME OVER !!! \n Press SPACE to Restart'
    start_game_text = 'Press SPACE to start'
class FontBuilder:
    @classmethod
    def font(cls, font_name, font_size):
        return pygame.font.SysFont(font_name, font_size)

    @classmethod
    def comic_sans(cls, size=30):
        return cls.font(Fonts.comic_sans.value, size)

class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    @classmethod
    def get_random_direction(cls):
        return random.choice([cls.UP, cls.DOWN, cls.RIGHT, cls.LEFT])

class Colors(Enum):
    GREEN = 'green'
    RED = 'red'
    WHITE = 'white'
    BLACK = 'black'