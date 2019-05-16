import random
import os
import time
from subprocess import call


# https://robertheaton.com/2018/07/20/project-2-game-of-life/

def create_row(length):
    row = []
    for i in range(length):
        row.append(0)
    return row


def dead_state(width, height):
    board = []
    for i in range(height):
        board.append(create_row(width))
    return board


def random_state(width, height):
    board = dead_state(width, height)
    for row in range(len(board)):
        for column in range(len(board[row])):
            random_number = random.random()
            if random_number <= .5:
                board[row][column] = 1
    return board


def print_board(board):
    call('clear' if os.name =='posix' else 'cls')
    for column in range(len(board[0])):
        print("---", end='')
    print("---")
    for row in range(len(board)):
        print("|", end='')
        for column in range(len(board[row])):
            if board[row][column] == 1:
                print(" # ", end='')
            else:
                print("   ", end='')
        print("|")
    for column in range(len(board[0])):
        print("---", end='')
    print("---")


def calculate_number_of_neighbors(board, location):
    neighbors = 0
    for i in range(-1, 2):
        x = location[0] + i
        for j in range(-1, 2):
            y = location[1] + j
            # print("({},{}):{}".format(x, y, board[x][y]))
            if x == location[0] and y == location[1]:
                pass
            elif x >= 0 and y >= 0 and y < len(board[0]) and x < len(board):
                if board[x][y] == 1:
                    neighbors += 1
    return neighbors


def next_board_state(board):
    new_board = dead_state(len(board[0]), len(board))
    for row in range(len(board)):
        for column in range(len(board[row])):
            neighbors = calculate_number_of_neighbors(board, (row, column))
            alive = board[row][column]
            if alive:
                rules = {2: 1,
                         3: 1}

            else:
                rules = {3: 1}
            new_board[row][column] = rules.get(neighbors, 0)
    return new_board


def play_game():
    board = random_state(50, 35)
    while True:
        print_board(board)
        new_board = next_board_state(board)
        if new_board == board:
            break
        else:
            board = new_board
        time.sleep(.15)

play_game()
