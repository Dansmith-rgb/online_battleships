import numpy as np
from constants import ROWS, COLS

"""
Stores the state of the board
"""

class Boards():
    def __init__(self):
        """
        init the board by creating empty grid
        """
        self.board_1 = self.create_empty_board()
        self.board_2 = self.create_empty_board()
        self.player_1 = "r"
        self.player_2 = "b"
        self.ready = False

    def update(self, row, col, person):
        """
        updates a square on the grid

        :param row: row
        :type row: int
        :param col: column
        :type col: int
        :param person: person
        :type person: int
        """
        if person == self.board_1:
            self.board_1[row][col] = person
        else:
            self.board_2[row][col] = person

    def clear(self):
        """
        Clears grid
        """
        self.board_1 = self.create_empty_board()
        self.board_2 = self.create_empty_board()

    def create_empty_board(self):
        return np.zeros((ROWS, COLS))

    def get_board(self, board_1, board_2):
        """
        gets the data of the board
        :return: (int,int,int)[]
        """
        print(self.board_1)
        if board_1:
            return self.board_1
        elif board_2:
            return self.board_2
        else:
            return self.board_1 and self.board_2
        