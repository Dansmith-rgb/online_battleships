import sys
import pygame
from constants import *
from network import Network
import time

class Game():

    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        pygame.init()
        pygame.font.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Online battleships")
        self.pos = 0
        self.small_font = pygame.font.SysFont("comicsans", 50)
        self.boxes = [] 

    def menu_screen(self):
        """
        This is the menu screen function
        """
        run = True
        offline = False
        w = 500
        h = 100
        x = self.WIDTH / 2 - w / 2 
        y = self.HEIGHT / 2 - h / 2
        
        
        
        
        
        while run:
            
            
            if offline:
                off = self.small_font.render("Server Offline, Try Again Later...", 1,
                                        (255, 0, 0))
                self.win.blit(off, (WIDTH / 2 - off.get_width() / 2, 500))

            menu_bg_img_surf = pygame.image.load("imgs/battle_ships_menu.jpg").convert()
            self.win.blit(pygame.transform.scale(menu_bg_img_surf, (900,600)), (0,0))
            pygame.draw.rect(self.win,BLACK,(x,y,w,h), 0, border_radius=10)
            self.win.blit(self.small_font.render("Click here to start", True, (0,255,0)), (x+10,y+10))
            button = pygame.Rect(x,y,w,h)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    offline = False
                    mouse = event.pos
                    
                    
                    if button.collidepoint(event.pos):
                        #bo = self.connect()
                        print("Yo")
                        run = False
                        break
       
    def DrawGrid(self):
        
        BlockSize = 50
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*BlockSize+BlockSize, y*BlockSize+BlockSize, BlockSize, BlockSize)
                if len(self.boxes) < 100:
                    self.boxes.append(rect)
                print(self.boxes)
                pygame.draw.rect(self.win, WHITE, rect, 1)
                if x*BlockSize == 50:
                    self.win.blit(self.small_font.render("A", True, WHITE), (x*BlockSize+BlockSize-95,y*BlockSize+BlockSize-15))
                if y*BlockSize == 50:
                    self.win.blit(self.small_font.render("A", True, WHITE), (x*BlockSize+BlockSize+5,y*BlockSize+BlockSize-110))

        pygame.display.flip()  

    def click_grid(self, pos):
        x = pos[0]
        y = pos[1]
        for square in self.boxes:
            if square.collidepoint(x,y):
                return square.left, square.top 

    def DisplayBoardWindow(self):
        """
        This function draws most of the writing on the screen.

        :param player: The user
        :type player: string
        """
        run = True
        while run:
            self.DrawGrid()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    self.click_grid(pos)
        pygame.display.flip()
        

    def DisplayGuessesWindow(self, player):
        pass

    def connect(self):
        """
        connect to server function
        """
        global n
        n = Network()
        return n.boards

    def run(self, name):
        global player
        starting = True
        run = True
        #player = bo.start_user
        #bo = n.send("name " + name)
        clock = pygame.time.Clock()
        while starting:
            self.menu_screen()
            starting = False
            break

        board_bg = pygame.image.load('imgs/board_bg.jpg')
        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
        pygame.display.flip()
        
        while run:

            #bo = n.send("get")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            self.DisplayBoardWindow()
            """
            self.DisplayBoardWindow(self)
            if bo.player_ready == "False":
                print("Player not ready")
            """
        print("Hello")

        #n.disconnect()

if __name__ == '__main__':
    name = input("Please type your name: ")               
    Game().run(name)            