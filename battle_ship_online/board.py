import numpy as np
from constants import ROWS, COLS
import pygame

"""
Stores the state of the board
"""

class Game_data():
    def __init__(self):
        """
        init the board by creating empty grid
        """
        self.p1_board = self.create_empty_board()
        self.p2_board = self.p1_board
        self.p1Name = "player 1"
        self.p2Name = "player_2"
        self.ready = False
        self.boxes = []
        self.board={}

    def check_for_win(self, player):
        pass

    

    def clear(self):
        """
        Clears both boards
        """
        self.board_1 = self.create_empty_board()
        self.board_2 = self.create_empty_board()

    def create_empty_board(self):
        BlockSize = 50
        letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i,x in enumerate(letter):
            for index,y in enumerate(number):
                rect = pygame.Rect(int(i)*BlockSize+BlockSize+50, int(index)*BlockSize+BlockSize+50, BlockSize, BlockSize)
                if len(self.boxes) < 100:

                    self.boxes.append(rect)
                    key = x + str(y)
                    self.board[key] = [rect, "", ""]

        print(self.board)
        

    def get_board(self):
        """
        gets the data of the boards
        :return: (int,int,int)[]
        """
        print(self.board, end='\n')


Game_data()
