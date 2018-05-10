import random
import numpy


class Game:
    def __init__(self):
        self.score = 0
        self.field = self.get_field()

    def move_to_side(self):
        temp_field = numpy.zeros(
            (4, 4),
            dtype=numpy.int
        )
        for row in range(4):
            count = 0
            for col in range(4):
                if self.field[row][col] != 0:
                    temp_field[row][count] = self.field[row][col]
                    count += 1
        return temp_field

    def addition_cells(self):
        for row in range(4):
            for col in range(3):
                if self.field[row][col] == self.field[row][col+1] \
                        and self.field[row][col] != 0:
                    self.field[row][col] *= 2
                    self.field[row][col+1] = 0
                    self.score += self.field[row][col]
        return self.field

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

    def move_left(self):
        if self.can_move():
            self.field = self.move_to_side()
            self.field = self.addition_cells()
            self.field = self.move_to_side()
            self.field = self.new_cell(self.field)
        return self.field

    def move_right(self):
        self.field = self.field[..., ::-1]
        if self.can_move():
            self.field = self.move_to_side()
            self.field = self.addition_cells()
            self.field = self.move_to_side()
            self.field = self.new_cell(self.field)
        self.field = self.field[..., ::-1]
        return self.field

    def move_up(self):
        self.field = numpy.transpose(self.field)
        if self.can_move():
            self.field = self.move_to_side()
            self.field = self.addition_cells()
            self.field = self.move_to_side()
            self.field = self.new_cell(self.field)
        self.field = numpy.transpose(self.field)
        return self.field

    def move_down(self):
        self.field = numpy.transpose(self.field)
        self.field = self.field[..., ::-1]
        if self.can_move():
            self.field = self.move_to_side()
            self.field = self.addition_cells()
            self.field = self.move_to_side()
            self.field = self.new_cell(self.field)
        self.field = self.field[..., ::-1]
        self.field = numpy.transpose(self.field)
        return self.field

    def has_moves(self):
        for row in range(3):
            for col in range(3):
                if self.field[row][col] == self.field[row+1][col] \
                        or self.field[row][col+1] == self.field[row][col]:
                    return True
        for row in range(4):
            for col in range(4):
                if self.field[row][col] == 0:
                    return True
        for col in range(3):
            if self.field[3][col] == self.field[3][col+1]:
                return True
        for row in range(3):
            if self.field[row][3] == self.field[row+1][3]:
                return True
        return False

    def can_move(self):
        for row in range(0, 4):
            for col in range(1, 4):
                if self.field[row][col-1] == 0 and self.field[row][col] > 0:
                    return True
                elif self.field[row][col-1] == self.field[row][col] \
                        and self.field[row][col-1] != 0:
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
