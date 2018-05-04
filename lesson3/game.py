import random
import numpy


class Game:
    def __init__(self):
        self.score = 0

    def move_to_side(self, field):
        temp_field = numpy.zeros((4, 4), dtype=numpy.int)
        for row in range(4):
            count = 0
            for col in range(4):
                if field[row][col] != 0:
                    temp_field[row][count] = field[row][col]
                    count += 1
        return temp_field

    def addition_cells(self, field):
        for row in range(4):
            for col in range(3):
                if field[row][col] == field[row][col + 1] \
                        and field[row][col] != 0:
                    field[row][col] *= 2
                    field[row][col + 1] = 0
                    self.score += field[row][col]
        return field

    def new_cell(self, field):
        start_numbers = (2, 4)
        while True:
            rows = random.randint(0, 3)
            cols = random.randint(0, 3)
            if field[rows][cols] == 0:
                field[rows][cols] = numpy.random.choice(
                    start_numbers,
                    p=[0.9, 0.1]
                )
                break
        return field

    def move_left(self, field_left):
        field_left = self.move_to_side(field_left)
        field_left = self.addition_cells(field_left)
        field_left = self.move_to_side(field_left)
        field_left = self.new_cell(field_left)
        return field_left

    def move_right(self, field_right):
        field_right = field_right[..., ::-1]
        field_right = self.move_to_side(field_right)
        field_right = self.addition_cells(field_right)
        field_right = self.move_to_side(field_right)
        field_right = field_right[..., ::-1]
        field_right = self.new_cell(field_right)
        return field_right

    def move_up(self, field_up):
        field_up = numpy.transpose(field_up)
        field_up = self.move_to_side(field_up)
        field_up = self.addition_cells(field_up)
        field_up = self.move_to_side(field_up)
        field_up = numpy.transpose(field_up)
        field_up = self.new_cell(field_up)
        return field_up

    def move_down(self, field_down):
        field_down = numpy.transpose(field_down)
        field_down = field_down[..., ::-1]
        field_down = self.move_to_side(field_down)
        field_down = self.addition_cells(field_down)
        field_down = self.move_to_side(field_down)
        field_down = field_down[..., ::-1]
        field_down = numpy.transpose(field_down)
        field_down = self.new_cell(field_down)
        return field_down

    def has_moves(self, field_to_check):
        for row in range(3):
            for col in range(3):
                if field_to_check[row][col] == field_to_check[row + 1][col] \
                        or field_to_check[row][col + 1] == field_to_check[row][col]:
                    return True

        for row in range(4):
            for col in range(4):
                if field_to_check[row][col] == 0:
                    return True

        for col in range(3):
            if field_to_check[3][col] == field_to_check[3][col + 1]:
                return True

        for row in range(3):
            if field_to_check[row][3] == field_to_check[row + 1][3]:
                return True

        return False

    def get_score(self):
        return self.score

    def get_field(self):
        game_field = numpy.zeros(
            (4, 4),
            dtype=numpy.int
        )
        self.new_cell(game_field)
        self.new_cell(game_field)
        return game_field


def main():
    game = Game()
    field = game.get_field()
    while True:
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))

        print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))

        if not game.has_moves(field):
            print("No available moves left, game over.")
            break

        print("L, R, U, D - move")
        print("Q - exit")

        try:
            enter_move = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if enter_move in ('l', 'L'):
            field = game.move_left(field)
        elif enter_move in ('r', 'R'):
            field = game.move_right(field)
        elif enter_move in ('u', 'U'):
            field = game.move_up(field)
        elif enter_move in ('d', 'D'):
            field = game.move_down(field)
        elif enter_move in ('q', 'Q'):
            break

    print("Bye!")


if __name__ == '__main__':
    main()
