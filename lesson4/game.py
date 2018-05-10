import sys
import time
import pygame
from logic_game import logic

pygame.init()
pygame.display.set_caption("2048")


class Renderer:
    '''
        Класс для отображения игрового окна
    '''
    def __init__(self):
        self.game = logic.Game()
        self.window = pygame.display.set_mode((400, 500))
        self.my_font = pygame.font.SysFont("times new roman", 40)

    def get_color(self, number):
        '''
            Содержит цвета для ячеек
        '''
        color_dict = {
            0: (181, 181, 181),
            2: (213, 213, 213),
            4: (186, 213, 179),
            8: (156, 213, 142),
            16: (130, 213, 108),
            32: (103, 213, 75),
            64: (127, 213, 213),
            128: (127, 163, 213),
            256: (106, 102, 213),
            512: (155, 102, 213),
            1024: (212, 102, 213),
            2048: (212, 102, 137),
        }
        return color_dict[number]

    def show_text(self):
        '''
            Расположение ячеек в нужной части окна и с необходимым
            значением
        '''
        for row in range(0, 4):
            for col in range(0, 4):
                pygame.draw.rect(self.window,
                                 self.get_color(self.game.field[col][row]),
                                 (row*(400/4), col*(400/4)+100, 400/4, 400/4))
                pygame.draw.rect(self.window,
                                 (188, 247, 173),
                                 (row*(400/4), col*(400/4)+100, 400/4, 400/4),
                                 1)
                if self.game.field[col][row] == 0:
                    text = self.my_font.render(" ", True, (0, 0, 0))
                else:
                    text = self.my_font.render(
                        str(self.game.field[col][row]),
                        True,
                        (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.centerx = row*(400/4)+45
                text_rect.centery = col*(400/4)+145
                text_score = self.my_font.render(
                    "Score: " + str(self.game.score),
                    1,
                    (255, 255, 255))
                self.window.blit(text, text_rect)
                self.window.blit(text_score, (10, 20))

    def game_over(self):
        '''
            Выводит конец игры
        '''
        over = self.my_font.render("GAME OVER", True, (0, 0, 0))
        text_over = over.get_rect()
        text_over.centerx = self.window.get_rect().centerx
        text_over.centery = self.window.get_rect().centery
        self.window.blit(over, text_over)


def main():
    game_field = Renderer()
    game_field.window.fill(game_field.get_color(0))
    game_field.show_text()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game_field.window.fill(game_field.get_color(0))
            if game_field.game.has_moves():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        game_field.game.field = game_field.game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        game_field.game.field = game_field.game.move_right()
                    elif event.key == pygame.K_UP:
                        game_field.game.field = game_field.game.move_up()
                    elif event.key == pygame.K_DOWN:
                        game_field.game.field = game_field.game.move_down()
                game_field.show_text()
            else:
                game_field.show_text()
                game_field.game_over()
        pygame.display.update()
        time.sleep(0.02)


if __name__ == '__main__':
    main()
