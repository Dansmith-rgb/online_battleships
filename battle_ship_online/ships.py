import pygame
from constants import *

class Ship:
    def __init__(self):
        self.placement_list = []
        self.ship_dragging = False

    def update_valid_placement(self, board):
        self.placement_list = self.valid_placement(board)


class Carrier(Ship):
    def __init__(self, board, row, col, colour, x, y):
        Ship.__init__(self)
        self.ship_length = 5
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour
        self.rect_1 = pygame.rect.Rect(600,200,50,50)

    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y):
            return True

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y

    def draw_ship(self, board):
        #self.rect_1 = pygame.Rect(x,y,50,50)
        
        pygame.draw.rect(board, BLACK, self.rect_1, 0)

    def change_orientation(self, board):
        pass

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
        self.rect_1 = pygame.Rect(170,170,50,50)

    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y):
            return True

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y
    
    def draw_ship(self, board):
        #self.rect_1 = pygame.Rect(x,y,50,50)
        pygame.draw.rect(board, BLACK, self.rect_1, 0)

    def change_orientation(self, board):
        pass

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
        self.rect_1 = pygame.Rect(220,220,50,50)

    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y):
            return True

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y

    def draw_ship(self, board):
        #self.rect_1 = pygame.Rect(x,y,50,50)
        pygame.draw.rect(board, BLACK, self.rect_1, 0)

    def change_orientation(self, board):
        pass

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
        self.rect_1 = pygame.Rect(70,70,50,50)
    
    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y):
            return True

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y

    def draw_ship(self, board):
        #self.rect_1 = pygame.Rect(x,y,50,50)
        pygame.draw.rect(board, BLACK, self.rect_1, 0)

    def change_orientation(self, board):
        pass

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
        self.rect_1 = pygame.Rect(270,270,50,50)

    def collide(self, x, y):
        if self.rect_1.collidepoint(x, y):
            return True

    def update_move(self, x,y):
        self.rect_1.x = x
        self.rect_1.y = y

    def draw_ship(self, board):
        #self.rect_1 = pygame.Rect(x,y,50,50)
        pygame.draw.rect(board, BLACK, self.rect_1, 0)

    def change_orientation(self, board):
        if self.ship_orientation == "horizontal":
            self.ship_orientation = "vertical"
        else:
            self.ship_orientation = "horizontal"

    def valid_placement(self, board):
        pass