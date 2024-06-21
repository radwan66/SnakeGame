import pygame
import random
from settings import Colors, TimeSettings, Screen

class Obstacle:
    def __init__(self, num_obstacles=5):
        self.obstacles = [self.random_position() for _ in range(num_obstacles)]

    def random_position(self):
        return (round(random.randrange(0, Screen.WIDTH - TimeSettings.SNAKE_BLOCK) / TimeSettings.SNAKE_BLOCK) * TimeSettings.SNAKE_BLOCK,
                round(random.randrange(0, Screen.HEIGHT - TimeSettings.SNAKE_BLOCK) / TimeSettings.SNAKE_BLOCK) * TimeSettings.SNAKE_BLOCK)

    def draw(self):
        for obs in self.obstacles:
            pygame.draw.rect(Screen.DIS, Colors.OBSTACLE, [obs[0], obs[1], TimeSettings.SNAKE_BLOCK, TimeSettings.SNAKE_BLOCK])
