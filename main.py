# Это игра сгенерирована DeepSeek
# TODO: Нужно проверить логику работы игры!
###########################################

import pygame
import random

# Constants
CELL_SIZE = 20
ROWS, COLS = 20, 20
GAME_WIDTH = CELL_SIZE * COLS
GAME_HEIGHT = CELL_SIZE * ROWS

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.reset_game()

    def reset_game(self):
        self.direction = RIGHT
        self.snake = [
            [COLS // 2, ROWS // 2],
            [COLS // 2 - 1, ROWS // 2],
            [COLS // 2 - 2, ROWS // 2]
        ]
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        while True:
            food_pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
            if food_pos not in self.snake:
                return food_pos

    def draw_grid(self):
        for x in range(0, GAME_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, GAME_HEIGHT))
        for y in range(0, GAME_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (GAME_WIDTH, y))

    def draw_snake(self):
        for segment in self.snake:
            x, y = segment[0] * CELL_SIZE, segment[1] * CELL_SIZE
            pygame.draw.rect(self.screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    def draw_food(self):
        x, y = self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE
        pygame.draw.rect(self.screen, RED, (x, y, CELL_SIZE, CELL_SIZE))

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(text, (10, 10))

    def draw_game_over(self):
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over!", True, WHITE)
        self.screen.blit(text, (GAME_WIDTH // 2 - 100, GAME_HEIGHT // 2 - 24))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(text, (GAME_WIDTH // 2 - 50, GAME_HEIGHT // 2 + 24))
        pygame.display.flip()
        self.game_over = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if not self.game_over:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    if event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    if event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    if event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT
                if event.key == pygame.K_r:
                    self.reset_game()

    def move_snake(self):
        head = self.snake[0].copy()
        head[0] += self.direction[0]
        head[1] += self.direction[1]
        self.snake.insert(0, head)
        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def check_collisions(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= COLS or head[1] < 0 or head[1] >= ROWS:
            self.draw_game_over()
        for segment in self.snake[1:]:
            if head == segment:
                self.draw_game_over()

    def run(self):
        while True:
            self.handle_events()
            if not self.game_over:
                self.move_snake()
                self.check_collisions()
                self.screen.fill(BLACK)
                self.draw_grid()
                self.draw_snake()
                self.draw_food()
                self.draw_score()
            pygame.display.flip()
            self.clock.tick(10)


game = SnakeGame()
game.run()
