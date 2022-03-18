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
        self.p1Name = "player 1"
        self.p2Name = "player_2"
        self.ready = False

    def check_for_win(self, player):
        pass

    def drop_ship(self, player):
        pass

    def clear(self):
        """
        Clears both boards
        """
        self.board_1 = self.create_empty_board()
        self.board_2 = self.create_empty_board()

    def create_empty_board(self):
        return np.zeros((ROWS, COLS))

    def get_board(self, board_1=False, board_2=False):
        """
        gets the data of the boards
        :return: (int,int,int)[]
        """
        print(self.board_1)
        if board_1:
            return self.board_1
        elif board_2:
            return self.board_2
        else:
            return self.board_1 and self.board_2
        