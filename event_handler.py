import pygame
from settings import TimeSettings

class EventHandler:
    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and game.x1_change == 0:
                    game.x1_change, game.y1_change = -TimeSettings.SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT and game.x1_change == 0:
                    game.x1_change, game.y1_change = TimeSettings.SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP and game.y1_change == 0:
                    game.y1_change, game.x1_change = -TimeSettings.SNAKE_BLOCK, 0
                elif event.key == pygame.K_DOWN and game.y1_change == 0:
                    game.y1_change, game.x1_change = TimeSettings.SNAKE_BLOCK, 0
