import pygame
from settings import Colors, TimeSettings, Screen

class Snake:
    def __init__(self):
        self.snake_list = []
        self.length_of_snake = 1

    def draw(self):
        for idx, x in enumerate(self.snake_list):
            color = Colors.SNAKE_HEAD if idx == len(self.snake_list) - 1 else Colors.SNAKE_BODY
            pygame.draw.circle(Screen.DIS, color, (x[0] + TimeSettings.SNAKE_BLOCK // 2, x[1] + TimeSettings.SNAKE_BLOCK // 2), TimeSettings.SNAKE_BLOCK // 2)

    def move(self, x1, y1):
        snake_head = [x1, y1]
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

    def check_collision(self):
        for x in self.snake_list[:-1]:
            if x == self.snake_list[-1]:
                return True
        return False
