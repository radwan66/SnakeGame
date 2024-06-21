import pygame
from settings import Colors, Screen, TimeSettings, Difficulty
from snake import Snake
from food import Food, PowerUp
from obstacle import Obstacle
from render import Renderer
from event_handler import EventHandler

class SnakeGame:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.power_up = PowerUp()
        self.obstacles = Obstacle()
        self.renderer = Renderer()
        self.event_handler = EventHandler()
        self.game_over = False
        self.game_close = False
        self.x1 = Screen.WIDTH / 2
        self.y1 = Screen.HEIGHT / 2
        self.x1_change = 0
        self.y1_change = 0
        self.snake_speed = Difficulty.EASY  # Default difficulty

    def update(self):
        self.x1 += self.x1_change
        self.y1 += self.y1_change

        if self.x1 >= Screen.WIDTH:
            self.x1 = 0
        elif self.x1 < 0:
            self.x1 = Screen.WIDTH - TimeSettings.SNAKE_BLOCK
        if self.y1 >= Screen.HEIGHT:
            self.y1 = 0
        elif self.y1 < 0:
            self.y1 = Screen.HEIGHT - TimeSettings.SNAKE_BLOCK

        self.snake.move(self.x1, self.y1)
        if self.snake.check_collision() or self.check_obstacle_collision():
            self.game_close = True

        if self.x1 == self.food.x and self.y1 == self.food.y:
            self.food = Food()
            self.snake.length_of_snake += 1

        if self.x1 == self.power_up.x and self.y1 == self.power_up.y:
            self.power_up = PowerUp()
            self.snake.length_of_snake += 3  # Increase length by 3

    def check_obstacle_collision(self):
        for obs in self.obstacles.obstacles:
            if self.x1 == obs[0] and self.y1 == obs[1]:
                return True
        return False

    def run(self):
        while not self.game_over:
            while self.game_close:
                Screen.DIS.fill(Colors.BACKGROUND)
                self.renderer.show_message("You Lost! Press Q-Quit or C-Play Again")
                self.renderer.display_score(self.snake.length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.__init__()

            self.event_handler.handle_events(self)
            self.update()
            self.renderer.render(self)
            TimeSettings.CLOCK.tick(self.snake_speed)

    def set_difficulty(self, difficulty):
        if difficulty == "EASY":
            self.snake_speed = Difficulty.EASY
        elif difficulty == "MEDIUM":
            self.snake_speed = Difficulty.MEDIUM
        elif difficulty == "HARD":
            self.snake_speed = Difficulty.HARD
