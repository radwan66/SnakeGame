import pygame
import random
from settings import Colors, TimeSettings, Screen

class Food:
    def __init__(self):
        self.x, self.y = self.random_position()

    def random_position(self):
        return (round(random.randrange(0, Screen.WIDTH - TimeSettings.SNAKE_BLOCK) / TimeSettings.SNAKE_BLOCK) * TimeSettings.SNAKE_BLOCK,
                round(random.randrange(0, Screen.HEIGHT - TimeSettings.SNAKE_BLOCK) / TimeSettings.SNAKE_BLOCK) * TimeSettings.SNAKE_BLOCK)

    def draw(self):
        pygame.draw.circle(Screen.DIS, Colors.FOOD, (self.x + TimeSettings.SNAKE_BLOCK // 2, self.y + TimeSettings.SNAKE_BLOCK // 2), TimeSettings.SNAKE_BLOCK // 2)

class PowerUp:
    def __init__(self):
        self.x, self.y = self.random_position()

    def random_position(self):
        return (round(random.randrange(0, Screen.WIDTH - TimeSettings.SNAKE_BLOCK) / TimeSettings.SNAKE_BLOCK) * TimeSettings.SNAKE_BLOCK,
                round(random.randrange(0, Screen.HEIGHT - TimeSettings.SNAKE_BLOCK) / TimeSettings.SNAKE_BLOCK) * TimeSettings.SNAKE_BLOCK)

    def draw(self):
        pygame.draw.circle(Screen.DIS, Colors.POWER_UP, (self.x + TimeSettings.SNAKE_BLOCK // 2, self.y + TimeSettings.SNAKE_BLOCK // 2), TimeSettings.SNAKE_BLOCK // 2)
