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
        self.board = self.create_empty_board()
        self.p1Name = "player 1"
        self.p2Name = "player_2"
        self.ready = False

    def check_for_win(self, player):
        pass

    

    def clear(self):
        """
        Clears both boards
        """
        self.board_1 = self.create_empty_board()
        self.board_2 = self.create_empty_board()

    def create_empty_board(self):
        matrix = []
        for i in range(ROWS):
            matrix.append([0] * COLS)
        for i in range(ROWS):
            matrix.append([1] * COLS)

        print(matrix)
        return matrix
        

    def get_board(self):
        """
        gets the data of the boards
        :return: (int,int,int)[]
        """
        print(self.board, end='\n')


Boards().create_empty_board()