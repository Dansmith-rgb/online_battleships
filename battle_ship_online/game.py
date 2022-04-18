import sys
import pygame
from constants import *
from network import Network
import time
from ships import *



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
        self.ships = [Submarine(self.win, 700, 200, "1"), Destroyer(self.win, 710, 210, "1"), Cruiser(self.win, 720, 220, "1"), Battleship(self.win, 730, 230, "1"), Carrier(self.win, 740, 240, "1", 100, 100)]
        self.current_ship = [None]
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
        letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        num = 0
        num2 = 0
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*BlockSize+BlockSize+50, y*BlockSize+BlockSize+50, BlockSize, BlockSize)
                if len(self.boxes) < 100:
                    self.boxes.append(rect)
                
                pygame.draw.rect(self.win, WHITE, rect, 1)
                
                
                if num2 <= 9:
                    self.win.blit(self.small_font.render(number[num2], True, WHITE), (x*BlockSize+BlockSize-5,y*BlockSize+BlockSize + 38))
                    num2 += 1

                
                
                

                    
                
    
            self.win.blit(self.small_font.render(letter[num], True, WHITE), (x*BlockSize+BlockSize+60,y*BlockSize-410))
            
            
            if num != 9:
                num += 1

            

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
        rect = pygame.Rect(630, 150, 276, 350)
        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
        while run:
            
            self.DrawGrid()
            
            self.SideBar("BoardWindow")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    print(self.click_grid(pos))
                    
        

    def SideBar(self, screen):
        if screen == "guesses":
            pass
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if event.button == 1:
                        for ship in self.ships:
                            if ship.collide(pos[0], pos[1]):
                                ship.ship_dragging = True
                                if len(self.current_ship) >= 1:
                                    del self.current_ship[0]
                                self.current_ship.append(ship)
                                break
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    x = pos[0]
                    y = pos[1]
                    if event.button == 1:
                        for ship in self.ships:
                            ship.ship_dragging = False
                elif event.type == pygame.MOUSEMOTION:
                    for ship in self.ships:
                        if ship.ship_dragging:
                            pos = event.pos
                            x = pos[0]
                            y = pos[1]
                            
                            print(self.current_ship)
                            if self.current_ship != [None]:
                                print(self.current_ship)
                                print(x,y)
                                #del self.current_ship[1]
                                board_bg = pygame.image.load('imgs/board_bg.jpg')
                                self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                rect = pygame.Rect(630, 150, 276, 350)
                                pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                self.current_ship[0].update_move(x,y)
                    


                
                try:
                    for ship in self.ships:
                        ship.draw_ship(self.win)
                except:
                    pass
                    
                        
                    

            pass
        
        
        

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
        
        
        while run:

            #bo = n.send("get")
            """
            if player.colour == "1":
                self.ships = [Submarine(self.win, 700, 200, "1"), Destroyer(self.win, 710, 210, "1"), Cruiser(self.win, 720, 220, "1"), Battleship(self.win, 730, 230, "1"), Carrier(self.win, 740, 240, "1")]
                
            else:
                self.ships = [Submarine(self.win, 700, 200, "2"), Destroyer(self.win, 710, 210, "2"), Cruiser(self.win, 720, 220, "2"), Battleship(self.win, 730, 230, "2"), Carrier(self.win, 740, 240, "2")]
            """
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            
            self.DisplayBoardWindow()
            
            pygame.display.flip()
            #if bo.player_ready == "False":
                #print("Player not ready")
            
        print("Hello")

        #n.disconnect()



if __name__ == '__main__':
    name = input("Please type your name: ")               
    Game().run(name)
     

