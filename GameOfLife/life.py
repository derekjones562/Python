import random
import os
import time
from subprocess import call


# https://robertheaton.com/2018/07/20/project-2-game-of-life/

class Board(object):

    def __init__(self, new_board, randomize=False):
        self.width = len(new_board[0])
        self.height = len(new_board)
        if randomize:
            self.board = self.random_state()
        else:
            self.board = new_board
        self._old_board = []
        self._stable = False

    def __str__(self):
        board_as_string = ""
        call('clear' if os.name == 'posix' else 'cls')
        for column in range(self.width):
            board_as_string += "---"
        board_as_string += "---\n"
        for row in range(self.height):
            board_as_string += "|"
            for column in range(self.width):
                if self.board[row][column] == 1:
                    board_as_string += " # "
                else:
                    board_as_string += "   "
            board_as_string += "|\n"
        for column in range(self.width):
            board_as_string += "---"
        board_as_string += "---\n"
        return board_as_string

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def _create_dead_row(width):
        row = []
        for i in range(width):
            row.append(0)
        return row

    @staticmethod
    def dead_state(width, height):
        dead_board = []
        for i in range(height):
            dead_board.append(Board._create_dead_row(width))
        return dead_board

    def random_state(self):
        random_board = self.dead_state(self.width, self.height)
        for row in range(self.height):
            for column in range(self.width):
                random_number = random.random()
                if random_number <= .5:
                    random_board[row][column] = 1
        return random_board

    def _calculate_number_of_neighbors(self, location):
        neighbors = 0
        for i in range(-1, 2):
            x = location[0] + i
            for j in range(-1, 2):
                y = location[1] + j
                # print("({},{}):{}".format(x, y, board[x][y]))
                if x == location[0] and y == location[1]:
                    pass
                elif x >= 0 and y >= 0 and y < self.width and x < self.height:
                    if self.board[x][y] == 1:
                        neighbors += 1
        return neighbors

    def next_board_state(self):
        new_board = self.dead_state(self.width, self.height)
        for row in range(self.height):
            for column in range(self.width):
                neighbors = self._calculate_number_of_neighbors((row, column))
                alive = self.board[row][column]
                if alive:
                    rules = {2: 1,
                             3: 1}

                else:
                    rules = {3: 1}
                new_board[row][column] = rules.get(neighbors, 0)
        return new_board

    def is_stable(self):
        return self._stable

    def play_game(self):
        print(self.__str__())
        new_board = self.next_board_state()
        if new_board == self.board or new_board == self._old_board:
            self._stable = True
        self._old_board = self.board
        self.board = new_board
        time.sleep(.15)

    def load(self, filename):
        with open(filename, "r") as file:
            board_from_file = []
            for line in file.readlines():
                row = []
                for char in line:
                    if char == '0' or char == '1':
                        row.append(int(char))
                board_from_file.append(row)
        return board_from_file



#filename = "./boardTemplates/toad.txt"
filename = "./boardTemplates/GosperGliderGun.txt"
board = Board(Board.dead_state(15, 15), True)
board = Board(board.load(filename))
#while not board.is_stable():
while True:
    board.play_game()
