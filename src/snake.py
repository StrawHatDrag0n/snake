import pygame
from utils import get_x, get_y
from constants import Direction, WIDTH, HEIGHT, SPEED, Colors, CELL_SIZE

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y, width=CELL_SIZE, height=CELL_SIZE, color=Colors.GREEN, direction=Direction.UP) -> None:
        super().__init__()
        self.color = color
        self.direction = direction
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color.value)
        self.rect = self.image.get_rect(x=x, y=y)

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    def update(self, *args, **kwargs) -> None:
        if self.direction is Direction.UP:
            self.rect.y = (self.rect.y - SPEED) % HEIGHT
        elif self.direction is Direction.DOWN:
            self.rect.y = (self.rect.y + SPEED) % HEIGHT
        elif self.direction is Direction.RIGHT:
            self.rect.x = (self.rect.x + SPEED) % WIDTH
        elif self.direction is Direction.LEFT:
            self.rect.x = (self.rect.x - SPEED) % WIDTH


class SnakeHeadSegment(SnakeSegment):
    def __init__(self, x, y, width=CELL_SIZE, height=CELL_SIZE, color=Colors.GREEN, direction=Direction.UP) -> None:
        super().__init__(x, y, width, height, color, direction)

    def update(self, new_direction) -> None:
        if new_direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = new_direction
        elif new_direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = new_direction
        elif new_direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = new_direction
        elif new_direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = new_direction
        super().update()


class SnakeBodySegment(SnakeSegment):
    def __init__(self, x, y, width=CELL_SIZE, height=CELL_SIZE, color=Colors.GREEN, direction=Direction.UP) -> None:
        super().__init__(x, y, width, height, color, direction)


class Snake:
    def __init__(self) -> None:
        self.snake_head: SnakeHeadSegment = SnakeHeadSegment(x=WIDTH // 2, y=HEIGHT // 2,
                                                             direction=Direction.get_random_direction())
        self.snake_body: list[SnakeBodySegment] = list()

    def get_head(self) -> SnakeHeadSegment:
        return self.snake_head

    def is_valid(self) -> bool:
        return not any(pygame.sprite.collide_rect(self.snake_head, segment) for segment in self.snake_body)

    def update(self, new_direction) -> None:
        direction = self.snake_head.direction
        self.snake_head.update(new_direction)
        for segment in self.snake_body:
            prev_direction = segment.direction
            segment.set_direction(direction)
            segment.update()
            direction = prev_direction

    def add(self) -> None:
        if self.snake_body:
            tail: SnakeSegment = self.snake_body[-1]
        else:
            tail: SnakeSegment = self.snake_head
        x, y = tail.direction.value
        self.snake_body.append(SnakeBodySegment(x=get_x(tail.rect.x, -1 * x), y=get_y(tail.rect.y, -1 * y)))

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.snake_head.image, self.snake_head.rect)
        for segment in self.snake_body:
            surface.blit(segment.image, segment.rect)


