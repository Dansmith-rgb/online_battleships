import pygame

class Ship:
    def __init__(self):
        self.placement_list = []
        self.ship_dragging = False

    def update_valid_placement(self, board):
        self.placement_list = self.valid_placement(board)

    def draw_ship(self, board, ship):
        pass

class Carrier(Ship):
    def __init__(self, board, row, col, colour):
        self.ship_length = 5
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour

    def change_orientation(self, board):
        pass

    def valid_placement(self, board):
        pass

class Battleship(Ship):
    def __init__(self, board, row , col, colour):
        self.ship_length = 4
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour

    def change_orientation(self, board):
        pass

    def valid_placement(self, board):
        pass

class Cruiser(Ship):
    def __init__(self, board, row, col, colour):
        self.ship_length = 3
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour

    def change_orientation(self, board):
        pass

    def valid_placement(self, board):
        pass

class Submarine(Ship):
    def __init__(self, board, row, col, colour):
        self.ship_length = 3
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour

    def change_orientation(self, board):
        pass

    def valid_placement(self, board):
        pass

class Destroyer(Ship):
    def __init__(self, board, row, col, colour):
        self.ship_length = 2
        self.ship_orientation = "horizontal"
        self.row = row
        self.col = col
        self.color = colour

    def change_orientation(self, board):
        if self.ship_orientation == "horizontal":
            self.ship_orientation = "vertical"
        else:
            self.ship_orientation = "horizontal"

    def start_pos(self, board):
        pass    

    def valid_placement(self, board):
        pass