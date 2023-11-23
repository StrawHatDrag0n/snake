import pygame
from bait import Bait
from snake import Snake
from utils import get_screen
from constants import Colors, FPS, HEIGHT, WIDTH, FontBuilder, Text, GameState, Direction

class GameInfo:
    def __init__(self):
        self.score = 0
        self.game_state = GameState.START

    def increase(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def change_game_state(self, new_game_state):
        self.game_state = new_game_state

class Game:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.screen = get_screen(width, height)
        self.state = GameInfo()
        self.snake = Snake()
        self.bait = Bait()
        self.clock = pygame.time.Clock()

    def reset(self):
        self.snake = Snake()
        self.bait = Bait()
        self.state.reset()

    def _loop(self, new_direction) -> GameInfo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        self.snake.update(new_direction)
        if not self.snake.is_valid():
            self.state.change_game_state(GameState.END)

        if self.state.game_state != GameState.PLAYING:
            return self.state

        if pygame.sprite.collide_rect(self.bait, self.snake.snake_head):
            self.snake.add()
            self.bait.update()
            self.state.increase()

        score_text_surface = (FontBuilder.comic_sans(size=30)
                              .render(Text.score_text.value.format(self.state.score),
                                                                    False,
                                                                    Colors.RED.value))
        self.screen.fill(Colors.BLACK.value)
        self.screen.blit(score_text_surface, (1, 1))
        self.snake.draw(self.screen)
        self.bait.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)
        return self.state

    def game_over_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.state.change_game_state(GameState.START)
                self.reset()

            if self.state.game_state != GameState.END:
                return
            game_over_surface = FontBuilder.comic_sans(size=50).render(Text.game_over_text.value, False,
                                                                       Colors.RED.value)
            self.screen.blit(game_over_surface, (
                WIDTH // 2 - game_over_surface.get_width() // 2, HEIGHT // 2 - game_over_surface.get_height() // 2))

            pygame.display.flip()

    def game_start_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.state.change_game_state(GameState.PLAYING)

            if self.state.game_state != GameState.START:
                return
            start_surface = FontBuilder.comic_sans(size=50).render(Text.start_game_text.value, False,
                                                                       Colors.RED.value)

            self.screen.blit(start_surface, (
                WIDTH // 2 - start_surface.get_width() // 2, HEIGHT // 2 - start_surface.get_height() // 2))
            pygame.display.flip()
    def run_state(self):
        while True:
            if self.state.game_state == GameState.START:
                self.game_start_screen()
            elif self.state.game_state == GameState.PLAYING:
                new_direction = None
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    new_direction = Direction.DOWN
                elif keys[pygame.K_UP]:
                    new_direction = Direction.UP
                elif keys[pygame.K_LEFT]:
                    new_direction = Direction.LEFT
                elif keys[pygame.K_RIGHT]:
                    new_direction = Direction.RIGHT
                self.state = self._loop(new_direction)
            elif self.state.game_state == GameState.END:
                self.game_over_screen()
    @staticmethod
    def run():
        pygame.display.set_caption("Snake")
        pygame.font.init()
        game = Game()
        game.run_state()


if __name__ == '__main__':
    pygame.init()
    Game.run()
