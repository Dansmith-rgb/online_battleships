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
        

    def collide(self, x, y):
        if self.rect_1.collidepoint(x,y) or self.rect_2.collidepoint(x,y) or self.rect_3.collidepoint(x,y) or self.rect_4.collidepoint(x,y) or self.rect_5.collidepoint(x,y):
            return True

    def reset(self):
        self.ship_orientation = "horizontal"
        self.rect_1 = pygame.Rect(640,161,50,50)
        self.rect_2 = pygame.Rect(690,161,50,50)
        self.rect_3 = pygame.Rect(740,161,50,50)
        self.rect_4 = pygame.Rect(790,161,50,50)
        self.rect_5 = pygame.Rect(840,161,50,50)

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
        

    def valid_placement(self, board):
        pass

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


    def valid_placement(self, board):
        pass

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


    def valid_placement(self, board):
        pass

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


    def valid_placement(self, board):
        pass

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

    

    def valid_placement(self, board):
        pass