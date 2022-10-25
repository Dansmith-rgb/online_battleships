import pygame
from constants import *
import json

class Ship:
    def __init__(self):
        self.placement_list = []
        self.ship_dragging = False

    def update_valid_placement(self, board):
        self.placement_list = self.valid_placement(board)

    def change_orientation(self, board):
        if self.ship_orientation == "horizontal":
            self.ship_orientation = "vertical"
            
        else:
            self.ship_orientation = "horizontal"

    def valid_placement(self, square, be_board):
        
        if be_board == 0 or be_board==1:
            if self.ship_orientation == "horizontal":
                if self.ship_length == 2:
                    if square.left == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 3:
                    if square.left == 500 or square.left == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 3:
                    if square.left == 500 or square.left == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 4:
                    if square.left == 450 or square.left == 500 or square.left == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 5:
                    if square.left == 400 or square.left == 450 or square.left == 500 or square.left == 550:
                        return False
                    else:
                        return True
            elif self.ship_orientation == "vertical":
                if self.ship_length == 2:
                    if square.top == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 3:
                    if square.top == 500 or square.top == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 3:
                    if square.top == 500 or square.top == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 4:
                    if square.top == 450 or square.top == 500 or square.top == 550:
                        return False
                    else:
                        return True
                if self.ship_length == 5:
                    if square.top == 400 or square.top == 450 or square.top == 500 or square.top == 550:
                        return False
                    else:
                        return True
            pass


class Carrier(Ship):
    def __init__(self, board, row, col, colour, x, y):
        Ship.__init__(self)
        self.ship_length = 5
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour
        self.rect_1 = pygame.Rect(640,161,50,50)
        self.rect_2 = pygame.Rect(690,161,50,50)
        self.rect_3 = pygame.Rect(740,161,50,50)
        self.rect_4 = pygame.Rect(790,161,50,50)
        self.rect_5 = pygame.Rect(840,161,50,50)
        #self.positions = [self.rect_1, self.rect_2, self.rect_3, self.rect_4, self.rect_5]
        
    
    def collide2(self, square, board, key, n, ship_name, player):
        if player == "1":
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "D"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "E"
                                    info4 = board.board[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "E"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "F"
                                    info4 = board.board[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "F"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "G"
                                    info4 = board.board[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "G"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "H"
                                    info4 = board.board[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "H"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "I"
                                    info4 = board.board[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "I"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "J"
                                    info4 = board.board[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "4"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "5"
                                    info4 = board.board[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "5"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "6"
                                    info4 = board.board[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "3":
                        new_key = "4"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "5"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "6"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "7"
                                    info4 = board.board[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "7"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "8"
                                    info4 = board.board[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "8"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "9"
                                    info4 = board.board[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "9"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "10"
                                    info4 = board.board[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
        else:
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "D"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "E"
                                    info4 = board.board_2[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "E"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "F"
                                    info4 = board.board_2[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "F"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "G"
                                    info4 = board.board_2[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "G"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "H"
                                    info4 = board.board_2[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "H"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "I"
                                    info4 = board.board_2[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "I"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    new_key_4 = "J"
                                    info4 = board.board_2[new_key_4+key[1]]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                        n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                        n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                        n.send(f"update {info4[1]} {new_key_4+key[1]} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "4"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "5"
                                    info4 = board.board_2[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "5"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "6"
                                    info4 = board.board_2[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "3":
                        new_key = "4"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "5"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "6"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "7"
                                    info4 = board.board_2[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "7"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "8"
                                    info4 = board.board_2[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "8"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "9"
                                    info4 = board.board_2[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "9"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    new_key_4 = "10"
                                    info4 = board.board_2[key[0]+new_key_4]
                                    if info4[1] == "":
                                        info4[1] = "Carrier"
                                        info3[1] = "Carrier"
                                        info2[1] = "Carrier"
                                        info1[1] = "Carrier"
                                        n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                        n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                        n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                        n.send(f"update {info4[1]} {key[0]+new_key_4} {player}")
                                        n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                
                    

    
    def collide(self,x,y):
        if self.rect_1.collidepoint(x,y) or self.rect_2.collidepoint(x,y) or self.rect_3.collidepoint(x,y) or self.rect_4.collidepoint(x,y) or self.rect_5.collidepoint(x,y):
                return True

    def reset(self):
        self.ship_orientation = "horizontal"
        self.rect_1 = pygame.Rect(640,161,50,50)
        self.rect_2 = pygame.Rect(690,161,50,50)
        self.rect_3 = pygame.Rect(740,161,50,50)
        self.rect_4 = pygame.Rect(790,161,50,50)
        self.rect_5 = pygame.Rect(840,161,50,50)
    """
    def check_no_ship(self):
        for length in range(2,5):
            if length == 3:
                if self.rect_1
    """
    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y
        if self.ship_orientation == "horizontal":

            
            self.rect_2.x = self.rect_1.x + 50
            self.rect_2.y = self.rect_1.y
            
            self.rect_3.x = self.rect_2.x + 50
            self.rect_3.y = self.rect_2.y
            self.rect_4.x = self.rect_3.x + 50
            self.rect_4.y = self.rect_3.y
            self.rect_5.x = self.rect_4.x + 50
            self.rect_5.y = self.rect_4.y
        else:
            self.rect_2.x = self.rect_1.x
            self.rect_2.y = self.rect_1.y + 50
            self.rect_3.x = self.rect_2.x
            self.rect_3.y = self.rect_2.y + 50
            self.rect_4.x = self.rect_3.x
            self.rect_4.y = self.rect_3.y + 50
            self.rect_5.x = self.rect_4.x
            self.rect_5.y = self.rect_4.y + 50

    def draw_ship(self, board):
        pygame.draw.rect(board, BLACK, self.rect_1, 0)
        pygame.draw.rect(board, BLACK, self.rect_2, 0)
        pygame.draw.rect(board, BLACK, self.rect_3, 0)
        pygame.draw.rect(board, BLACK, self.rect_4, 0)
        pygame.draw.rect(board, BLACK, self.rect_5, 0)

        

class Battleship(Ship):
    def __init__(self, board, row , col, colour):
        Ship.__init__(self)
        self.ship_length = 4
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour
        self.rect_1 = pygame.Rect(640,228,50,50)
        self.rect_2 = pygame.Rect(690,228,50,50)
        self.rect_3 = pygame.Rect(740,228,50,50)
        self.rect_4 = pygame.Rect(790,228,50,50)
        self.positions = [self.rect_1, self.rect_2, self.rect_3, self.rect_4]

    def collide2(self, square, board, key, n, ship_name, player):
        if player == "1":
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "D"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "E"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "F"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "G"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False


                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "H"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False


                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "I"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    
                    if key[0] == "G":
                        new_key = "H"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "I"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "J"
                                info3 = board.board[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "4"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "5"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "3":
                        new_key = "4"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "5"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "6"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "7"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "8"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "9"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "7":
                        new_key = "8"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "9"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "10"
                                info3 = board.board[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
        else:
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "D"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "E"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "F"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "G"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False


                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "H"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False


                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "I"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    
                    if key[0] == "G":
                        new_key = "H"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "I"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                new_key_3 = "J"
                                info3 = board.board_2[new_key_3+key[1]]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                    n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                    n.send(f"update {info3[1]} {new_key_3+key[1]} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "4"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "5"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "3":
                        new_key = "4"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "5"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "6"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "7"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "8"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "9"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "7":
                        new_key = "8"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "9"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                new_key_3 = "10"
                                info3 = board.board_2[key[0]+new_key_3]
                                if info3[1] == "":
                                    info3[1] = "Battleship"
                                    info2[1] = "Battleship"
                                    info1[1] = "Battleship"
                                    n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                    n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                    n.send(f"update {info3[1]} {key[0]+new_key_3} {player}")
                                    n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False


    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y) or self.rect_2.collidepoint(x,y) or self.rect_3.collidepoint(x,y) or self.rect_4.collidepoint(x,y):
            return True

    def reset(self):
        self.ship_orientation = "horizontal"
        self.rect_1 = pygame.Rect(640,228,50,50)
        self.rect_2 = pygame.Rect(690,228,50,50)
        self.rect_3 = pygame.Rect(740,228,50,50)
        self.rect_4 = pygame.Rect(790,228,50,50)

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y
        if self.ship_orientation == "horizontal":
            self.rect_2.x = self.rect_1.x + 50
            self.rect_2.y = self.rect_1.y
            self.rect_3.x = self.rect_2.x + 50
            self.rect_3.y = self.rect_2.y
            self.rect_4.x = self.rect_3.x + 50
            self.rect_4.y = self.rect_3.y
        else:
            self.rect_2.x = self.rect_1.x
            self.rect_2.y = self.rect_1.y + 50
            self.rect_3.x = self.rect_2.x
            self.rect_3.y = self.rect_2.y + 50
            self.rect_4.x = self.rect_3.x
            self.rect_4.y = self.rect_3.y + 50
    
    def draw_ship(self, board):
        pygame.draw.rect(board, GREYLIGHT, self.rect_1, 0)
        pygame.draw.rect(board, GREYLIGHT, self.rect_2, 0)
        pygame.draw.rect(board, GREYLIGHT, self.rect_3, 0)
        pygame.draw.rect(board, GREYLIGHT, self.rect_4, 0)


class Cruiser(Ship):
    def __init__(self, board, row, col, colour):
        Ship.__init__(self)
        self.ship_length = 3
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour
        self.rect_1 = pygame.Rect(640,295,50,50)
        self.rect_2 = pygame.Rect(690,295,50,50)
        self.rect_3 = pygame.Rect(740,295,50,50)
        self.positions = [self.rect_1, self.rect_2, self.rect_3]

    
    def collide2(self, square, board, key, n, ship_name, player):
        if player == "1":
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
                    
                    if key[0] == "G":
                        new_key = "H"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "I"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "H":
                        new_key = "I"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "J"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "7":
                        new_key = "8"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "9"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "8":
                        new_key = "9"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "10"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
        else:
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
                    
                    if key[0] == "G":
                        new_key = "H"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "I"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "H":
                        new_key = "I"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "J"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "7":
                        new_key = "8"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "9"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "8":
                        new_key = "9"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "10"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Cruiser"
                                info1[1] = "Cruiser"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False


    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y) or self.rect_2.collidepoint(x, y) or self.rect_3.collidepoint(x, y):
            return True

    def reset(self):
        self.ship_orientation = "horizontal"
        self.rect_1 = pygame.Rect(640,295,50,50)
        self.rect_2 = pygame.Rect(690,295,50,50)
        self.rect_3 = pygame.Rect(740,295,50,50)

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y
        if self.ship_orientation == "horizontal":
            self.rect_2.x = self.rect_1.x + 50
            self.rect_2.y = self.rect_1.y
            self.rect_3.x = self.rect_2.x + 50
            self.rect_3.y = self.rect_2.y
        else:
            self.rect_2.x = self.rect_1.x
            self.rect_2.y = self.rect_1.y + 50
            self.rect_3.x = self.rect_2.x
            self.rect_3.y = self.rect_2.y + 50

    def draw_ship(self, board):
        pygame.draw.rect(board, GREYMEDIUM, self.rect_1, 0)
        pygame.draw.rect(board, GREYMEDIUM, self.rect_2, 0)
        pygame.draw.rect(board, GREYMEDIUM, self.rect_3, 0)


class Submarine(Ship):
    def __init__(self, board, row, col, colour):
        Ship.__init__(self)
        self.ship_length = 3
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour
        self.rect_1 = pygame.Rect(640,362,50,50)
        self.rect_2 = pygame.Rect(690,362,50,50)
        self.rect_3 = pygame.Rect(740,362,50,50)
        self.positions = [self.rect_1, self.rect_2, self.rect_3]

    def collide2(self, square, board, key, n, ship_name, player):
        if player == "1":
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
                    
                    if key[0] == "G":
                        new_key = "H"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "I"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "H":
                        new_key = "I"
                        
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "J"
                            info2 = board.board[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "7":
                        new_key = "8"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "9"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "8":
                        new_key = "9"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "10"
                            info2 = board.board[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
        else:
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "C"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "D"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "E"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "F"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "G"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "H"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
                    
                    if key[0] == "G":
                        new_key = "H"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "I"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[0] == "H":
                        new_key = "I"
                        
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            new_key_2 = "J"
                            info2 = board.board_2[new_key_2+key[1]]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                                n.send(f"update {info2[1]} {new_key_2+key[1]} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "3"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "4"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "4":
                        new_key = "5"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "6"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "7"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "8"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "7":
                        new_key = "8"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "9"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False

                    if key[1] == "8":
                        new_key = "9"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            new_key_2 = "10"
                            info2 = board.board_2[key[0]+new_key_2]
                            if info2[1] == "":
                                info2[1] = "Submarine"
                                info1[1] = "Submarine"
                                n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                                n.send(f"update {info2[1]} {key[0]+new_key_2} {player}")
                                n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                                return True
                            else:
                                return False
                        else:
                            return False
    
    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y):
            return True

    def reset(self):
        self.ship_orientation = "horizontal"
        self.rect_1 = pygame.Rect(640,362,50,50)
        self.rect_2 = pygame.Rect(690,362,50,50)
        self.rect_3 = pygame.Rect(740,362,50,50)

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y
        if self.ship_orientation == "horizontal":
            self.rect_2.x = self.rect_1.x + 50
            self.rect_2.y = self.rect_1.y
            self.rect_3.x = self.rect_2.x + 50
            self.rect_3.y = self.rect_2.y
        else:
            self.rect_2.x = self.rect_1.x
            self.rect_2.y = self.rect_1.y + 50
            self.rect_3.x = self.rect_2.x
            self.rect_3.y = self.rect_2.y + 50

    def draw_ship(self, board):
        pygame.draw.rect(board, GREYDARK, self.rect_1, 0)
        pygame.draw.rect(board, GREYDARK, self.rect_2, 0)
        pygame.draw.rect(board, GREYDARK, self.rect_3, 0)


    
class Destroyer(Ship):
    def __init__(self, board, row, col, colour):
        Ship.__init__(self)
        self.ship_length = 2
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour
        self.rect_1 = pygame.Rect(640,429,50,50)
        self.rect_2 = pygame.Rect(690,429,50,50)
        self.positions = [self.rect_1, self.rect_2]

    def collide2(self, square, board, key, n, ship_name, player):
        if player == "1":
            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "G":
                        new_key = "H"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "H":
                        new_key = "I"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "I":
                        new_key = "J"
                        info1 = board.board[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "3":
                        new_key = "4"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "8":
                        new_key = "9"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "9":
                        new_key = "10"

                        info1 = board.board[key[0]+new_key]
                        if info1[1] == "":
                            
                            info1[1] = "Destroyer"
                            #print(board.board)
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False
        
        else:

            if square[1] == "":
                square[1] = ship_name
                if self.ship_orientation == "horizontal":
                    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    #print(letters.index(key[0]) + 1)
                    if key[0] == "A":
                        new_key = "B"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "B":
                        new_key = "C"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "C":
                        new_key = "D"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "D":
                        new_key = "E"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "E":
                        new_key = "F"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "F":
                        new_key = "G"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "G":
                        new_key = "H"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "H":
                        new_key = "I"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[0] == "I":
                        new_key = "J"
                        info1 = board.board_2[new_key+key[1]]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {new_key+key[1]} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                else:
                    if key[1] == "1":
                        new_key = "2"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "2":
                        new_key = "3"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "3":
                        new_key = "4"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "5":
                        new_key = "6"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "6":
                        new_key = "7"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "8":
                        new_key = "9"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

                    if key[1] == "9":
                        new_key = "10"

                        info1 = board.board_2[key[0]+new_key]
                        if info1[1] == "":
                            info1[1] = "Destroyer"
                            n.send(f"update {info1[1]} {key[0]+new_key} {player}")
                            n.send(f"update {square[1]} {key[0]+key[1]} {player}")
                            return True
                        else:
                            return False

    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y) or self.rect_2.collidepoint(x, y):
            return True

    def reset(self):
        self.ship_orientation = "horizontal"
        self.rect_1 = pygame.Rect(640,429,50,50)
        self.rect_2 = pygame.Rect(690,429,50,50)

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y
        if self.ship_orientation == "horizontal":
            self.rect_2.x = self.rect_1.x + 50
            self.rect_2.y = self.rect_1.y
        else:
            self.rect_2.x = self.rect_1.x
            self.rect_2.y = self.rect_1.y + 50

    def draw_ship(self, board):
        pygame.draw.rect(board, GREYVDARK, self.rect_1, 0)
        pygame.draw.rect(board, GREYVDARK, self.rect_2, 0)


