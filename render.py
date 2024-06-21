import pygame
from settings import Colors, Screen, Fonts

class Renderer:
    def display_score(self, score):
        value = Fonts.SCORE_FONT.render("Your Score: " + str(score), True, Colors.TEXT)
        Screen.DIS.blit(value, [0, 0])

    def show_message(self, msg):
        mesg = Fonts.FONT_STYLE.render(msg, True, Colors.TEXT)
        Screen.DIS.blit(mesg, [Screen.WIDTH / 6, Screen.HEIGHT / 3])

    def render(self, game):
        Screen.DIS.fill(Colors.BACKGROUND)
        game.food.draw()
        game.power_up.draw()
        game.obstacles.draw()
        game.snake.draw()
        self.display_score(game.snake.length_of_snake - 1)
        pygame.display.update()
