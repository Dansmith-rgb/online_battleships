import numpy as np
from constants import ROWS, COLS, WHITE
import pygame
import copy

"""
Stores the state of the board
"""

class Game_data:
    def __init__(self):
        """
        init the board by creating empty grid
        """
        self.boxes = []
        self.boxes_2 = []
        self.board={}
        self.board_2 = {}
        self.create_empty_board_1()
        self.create_empty_board_2()
        self.p1Name = "player 1"
        self.p2Name = "player 2"
        self.ready = False
        self.turn = "1"
        

    def check_for_win(self, player):
        pass

    def check_guesses(self, board, key):
        
        #draw circle if not hit a ship
        print(board[key][2])
        if board[key][2] == "":
            
            
            if board[key][1] == "Carrier" or board[key][1] == "Battleship" or board[key][1] == "Submarine" or board[key][1] == "Destroyer" or board[key][1] == "Cruiser":
                
                board[key][2] = "Hit"
                #run = False
                #draw a cross if a ship was hit
                pass
            else:
                
                board[key][2] = "Miss"
                print("hello")
                #run = False
                
    

    def clear(self):
        """
        Clears both boards
        """
        self.board_1 = self.create_empty_board()
        self.board_2 = self.create_empty_board()

    def create_empty_board_1(self):
        BlockSize = 50
        letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i,x in enumerate(letter):
            for index,y in enumerate(number):
                rect = pygame.Rect(int(i)*BlockSize+BlockSize+50, int(index)*BlockSize+BlockSize+50, BlockSize, BlockSize)
                if len(self.boxes) < 100:

                    self.boxes.append(rect)
                    key = f"{x + str(y)}"
                    self.board[key] = [rect, "", ""]

        print(self.board)
        
    def create_empty_board_2(self):
        BlockSize = 50
        letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i,x in enumerate(letter):
            for index,y in enumerate(number):
                rect = pygame.Rect(int(i)*BlockSize+BlockSize+50, int(index)*BlockSize+BlockSize+50, BlockSize, BlockSize)
                if len(self.boxes_2) < 100:

                    self.boxes_2.append(rect)
                    key = x + str(y)
                    self.board_2[key] = [rect, "", ""]

        print(self.board)

    def get_board(self):
        """
        gets the data of the boards
        :return: (int,int,int)[]
        """
        print(self.board, end='\n')
