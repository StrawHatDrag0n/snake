import random
import pygame
from constants import Colors, CELL_SIZE, WIDTH, HEIGHT

class Bait(pygame.sprite.Sprite):
    def __init__(self, x=random.randint(0, WIDTH - CELL_SIZE), y=random.randint(0, HEIGHT - CELL_SIZE),
                 width=CELL_SIZE, height=CELL_SIZE, color=Colors.RED):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - CELL_SIZE),
                                random.randint(0, HEIGHT - CELL_SIZE),
                                CELL_SIZE, CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color.value, self.rect)