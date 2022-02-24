import pygame
import pickle
from board import Board

class Game(object):
    def __init__(self):
        self.board = Board()

    def update_board(self, row, col, person):
        """
        Calls update board method

        :param row: row
        :type row: int
        :param col: column
        :type col: int
        :param person: Person
        :type person: object
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(row, col, person)

Game().main()