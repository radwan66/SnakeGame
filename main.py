import pygame
from game import SnakeGame
from settings import Colors, Screen, Fonts

if __name__ == "__main__":
    game = SnakeGame()

    Screen.DIS.fill(Colors.BACKGROUND)
    msg = Fonts.FONT_STYLE.render("Select Difficulty: 1-EASY, 2-MEDIUM, 3-HARD", True, Colors.TEXT)
    Screen.DIS.blit(msg, [Screen.WIDTH / 6, Screen.HEIGHT / 3])
    pygame.display.update()

    selecting_difficulty = True
    while selecting_difficulty:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game.set_difficulty("EASY")
                    selecting_difficulty = False
                elif event.key == pygame.K_2:
                    game.set_difficulty("MEDIUM")
                    selecting_difficulty = False
                elif event.key == pygame.K_3:
                    game.set_difficulty("HARD")
                    selecting_difficulty = False

    game.run()

