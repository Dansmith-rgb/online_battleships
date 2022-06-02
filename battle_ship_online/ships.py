import pygame
from constants import *

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
        
    
    def collide2(self, square, board, key):
        if square[1] == "":
            if self.ship_orientation == "horizontal":
                letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                #print(letters.index(key[0]) + 1)
                if key[0] == "A":
                    new_key = "B"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "C"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "D"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                new_key = "E"
                                info4 = board[new_key+key[1]]
                                if info4[1] == "":
                                    info4[1] = "Carrier"
                                    info3[1] = "Carrier"
                                    info2[1] = "Carrier"
                                    info1[1] = "Carrier"
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
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "D"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "E"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                new_key = "F"
                                info4 = board[new_key+key[1]]
                                if info4[1] == "":
                                    info4[1] = "Carrier"
                                    info3[1] = "Carrier"
                                    info2[1] = "Carrier"
                                    info1[1] = "Carrier"
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
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "E"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "F"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                new_key = "G"
                                info4 = board[new_key+key[1]]
                                if info4[1] == "":
                                    info4[1] = "Carrier"
                                    info3[1] = "Carrier"
                                    info2[1] = "Carrier"
                                    info1[1] = "Carrier"
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
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "F"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "G"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                new_key = "H"
                                info4 = board[new_key+key[1]]
                                if info4[1] == "":
                                    info4[1] = "Carrier"
                                    info3[1] = "Carrier"
                                    info2[1] = "Carrier"
                                    info1[1] = "Carrier"
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
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "G"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "H"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                new_key = "I"
                                info4 = board[new_key+key[1]]
                                if info4[1] == "":
                                    info4[1] = "Carrier"
                                    info3[1] = "Carrier"
                                    info2[1] = "Carrier"
                                    info1[1] = "Carrier"
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
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "H"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "I"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                new_key = "J"
                                info4 = board[new_key+key[1]]
                                if info4[1] == "":
                                    info4[1] = "Carrier"
                                    info3[1] = "Carrier"
                                    info2[1] = "Carrier"
                                    info1[1] = "Carrier"
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

    def collide2(self, square, board, key):
        if square[1] == "":
            if self.ship_orientation == "horizontal":
                letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                #print(letters.index(key[0]) + 1)
                if key[0] == "A":
                    new_key = "B"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "C"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "D"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

                if key[0] == "B":
                    new_key = "C"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "D"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "E"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

                if key[0] == "C":
                    new_key = "D"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "E"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "F"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

                if key[0] == "D":
                    new_key = "E"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "F"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "G"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False


                if key[0] == "E":
                    new_key = "F"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "G"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "H"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False


                if key[0] == "F":
                    new_key = "G"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "H"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "I"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

                
                if key[0] == "G":
                    new_key = "H"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "I"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            new_key = "J"
                            info3 = board[new_key+key[1]]
                            if info3[1] == "":
                                info3[1] = "Battleship"
                                info2[1] = "Battleship"
                                info1[1] = "Battleship"
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
        pygame.draw.rect(board, BLACK, self.rect_1, 0)
        pygame.draw.rect(board, BLACK, self.rect_2, 0)
        pygame.draw.rect(board, BLACK, self.rect_3, 0)
        pygame.draw.rect(board, BLACK, self.rect_4, 0)


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

    
    def collide2(self, square, board, key):
        if square[1] == "":
            if self.ship_orientation == "horizontal":
                letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                #print(letters.index(key[0]) + 1)
                if key[0] == "A":
                    new_key = "B"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "C"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "B":
                    new_key = "C"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "D"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "C":
                    new_key = "D"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "E"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "D":
                    new_key = "E"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "F"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "E":
                    new_key = "F"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "G"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "F":
                    new_key = "G"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "H"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False
                
                if key[0] == "G":
                    new_key = "H"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "I"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "H":
                    new_key = "I"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "J"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Cruiser"
                            info1[1] = "Cruiser"
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
        pygame.draw.rect(board, BLACK, self.rect_1, 0)
        pygame.draw.rect(board, BLACK, self.rect_2, 0)
        pygame.draw.rect(board, BLACK, self.rect_3, 0)


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

    def collide2(self, square, board, key):
        if square[1] == "":
            if self.ship_orientation == "horizontal":
                letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                #print(letters.index(key[0]) + 1)
                if key[0] == "A":
                    new_key = "B"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "C"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "B":
                    new_key = "C"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "D"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "C":
                    new_key = "D"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "E"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "D":
                    new_key = "E"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "F"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "E":
                    new_key = "F"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "G"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "F":
                    new_key = "G"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "H"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False
                
                if key[0] == "G":
                    new_key = "H"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "I"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
                            return True
                        else:
                            return False
                    else:
                        return False

                if key[0] == "H":
                    new_key = "I"
                    
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        new_key = "J"
                        info2 = board[new_key+key[1]]
                        if info2[1] == "":
                            info2[1] = "Submarine"
                            info1[1] = "Submarine"
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
        pygame.draw.rect(board, BLACK, self.rect_1, 0)
        pygame.draw.rect(board, BLACK, self.rect_2, 0)
        pygame.draw.rect(board, BLACK, self.rect_3, 0)


    
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

    def collide2(self, square, board, key):
        if square[1] == "":
            if self.ship_orientation == "horizontal":
                letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                #print(letters.index(key[0]) + 1)
                if key[0] == "A":
                    new_key = "B"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "B":
                    new_key = "C"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "C":
                    new_key = "D"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "D":
                    new_key = "E"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "E":
                    new_key = "F"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "F":
                    new_key = "G"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "G":
                    new_key = "H"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "H":
                    new_key = "I"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
                        return True
                    else:
                        return False

                if key[0] == "I":
                    new_key = "J"
                    info1 = board[new_key+key[1]]
                    if info1[1] == "":
                        info1[1] = "Destroyer"
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
        pygame.draw.rect(board, BLACK, self.rect_1, 0)
        pygame.draw.rect(board, BLACK, self.rect_2, 0)


