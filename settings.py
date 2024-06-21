import pygame

pygame.init()

class Colors:
    BACKGROUND = (30, 30, 30)
    SNAKE_HEAD = (0, 255, 0)
    SNAKE_BODY = (0, 200, 0)
    FOOD = (255, 0, 0)
    OBSTACLE = (255, 255, 0)
    POWER_UP = (0, 0, 255)
    TEXT = (255, 255, 255)

class Screen:
    WIDTH = 600
    HEIGHT = 400
    DIS = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

class TimeSettings:
    CLOCK = pygame.time.Clock()
    SNAKE_BLOCK = 20

class Fonts:
    FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
    SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

class Difficulty:
    EASY = 8
    MEDIUM = 15
    HARD = 25
