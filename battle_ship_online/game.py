import sys
import pygame
from constants import *
from network import Network
import time
from ships import *
import tkinter.messagebox as tk
import tkinter


pygame.init()
class Game():

    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
        pygame.font.init()
        
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Online battleships")
        self.pos = 0
        self.big_font = pygame.font.SysFont("comicsans", 50)
        self.medium_font = pygame.font.SysFont("comicsans", 30)
        self.boxes = []
        self.ships = [Submarine(self.win, 5, 5, "1"), Destroyer(self.win, 4, 4, "1"), Cruiser(self.win, 720, 220, "1"), Battleship(self.win, 730, 230, "1"), Carrier(self.win, 740, 240, "1", 100, 100)]
        self.current_ship = [None]
        self.index_box = []
        self.mute_music = False
        self.leave = False
        #self.board = {"A1": ["", "Battleship","1"]}
        self.board = {}
        self.opppsition_board = {}
        
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
                off = self.big_font.render("Server Offline, Try Again Later...", 1,
                                        (255, 0, 0))
                self.win.blit(off, (WIDTH / 2 - off.get_width() / 2, 500))

            menu_bg_img_surf = pygame.image.load("imgs/battle_ships_menu.jpg").convert()
            self.win.blit(pygame.transform.scale(menu_bg_img_surf, (900,600)), (0,0))
            pygame.draw.rect(self.win,BLACK,(x,y,w,h), 0, border_radius=10)
            self.win.blit(self.big_font.render("Click here to start", True, (0,255,0)), (x+10,y+10))
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
        board_num = ""
        board_letter = ""
        #self.board = {board_num+board_letter: ["", "",""]}
        for i,x in enumerate(letter):
            for index,y in enumerate(number):
                
                rect = pygame.Rect(int(i)*BlockSize+BlockSize+50, int(index)*BlockSize+BlockSize+50, BlockSize, BlockSize)
                if len(self.boxes) < 100:

                    self.boxes.append(rect)
                    key = x + str(y)
                    self.board[key] = [rect, "", ""]
                    
                
                pygame.draw.rect(self.win, WHITE, rect, 1)
                
                
                if num2 <= 9:
                    board_num = letter[num]
                    self.win.blit(self.big_font.render(y, True, WHITE), (i*BlockSize+BlockSize-5,index*BlockSize+BlockSize + 38))
                    num2 += 1
                
            self.win.blit(self.big_font.render(x, True, WHITE), (i*BlockSize+BlockSize+60,index*BlockSize-410))
            
            
            if num != 9:
                num += 1
        x = 200
        y = 202
        

        
                

        pygame.display.flip()  

    def click_grid(self, pos):
        x = pos[0]
        y = pos[1]
        for key,square in self.board.items():
            if square[0].collidepoint(x,y):
                return key

    def about(self):
        run = True
        while run:
            self.win.fill(WHITE)
            title_about_surface = self.big_font.render('ABOUT', True, BLACK)
            self.win.blit(title_about_surface, (350,50))
            detail_about_surface = self.medium_font.render('This is a online game of battleships with all the original rules:).', True, BLACK)
            detail_about_surface_2 = self.medium_font.render('Perfect for playing a friend!!!', True, BLACK)
            back_button_img = pygame.image.load('imgs/back-button.png')
            back_button_rect = pygame.Rect(400,400,50,50)
            self.win.blit(pygame.transform.scale(back_button_img, (50,50)), (400, 400))
            self.win.blit(detail_about_surface, (4, 200))
            self.win.blit(detail_about_surface_2, (4, 245))
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_rect.collidepoint(*mouse):
                        run = False

            pygame.display.flip()

    

    def Pause_menu(self):
        run = True
        quit_button = pygame.Rect(425,400,50,50)
        about_button = pygame.Rect(self.WIDTH/2-100, self.HEIGHT/2-70, 200,70)
        while run:
            
            self.win.fill(WHITE)
            quit_button_img = pygame.image.load('imgs/quit.png')
            self.win.blit(pygame.transform.scale(quit_button_img, (50,50)), (425,400))
            pygame.draw.rect(self.win, WHITE, about_button)
            title_pause_surface = self.big_font.render('Online Battleships', True, BLACK)
            about_button_surface = self.big_font.render('ABOUT', True, BLACK)
            self.win.blit(about_button_surface, (self.WIDTH/2-92, self.HEIGHT/2-70))
            self.win.blit(title_pause_surface, (240, 40))
            back_button_img = pygame.image.load('imgs/back-button.png')
            back_button_rect = pygame.Rect(700,525,50,50)
            self.win.blit(pygame.transform.scale(back_button_img, (50,50)), (700, 525))
            music_button = pygame.Rect(780,525,50,50)
            if self.mute_music:
                music_on_img = pygame.image.load('imgs/volume.png')
                self.win.blit(pygame.transform.scale(music_on_img, (50,50)), (780,525))
            else:
                music_off_img = pygame.image.load('imgs/mute.png')
                self.win.blit(pygame.transform.scale(music_off_img, (50,50)), (780,525))
            
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        run = False
                        return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(event.pos):
                        run = False
                    if back_button_rect.collidepoint(event.pos):
                        
                        
                        root = tkinter.Tk()
                        root.overrideredirect(1)
                        root.withdraw()
                        answer = tk.askyesno("Leave the game?", "Are you sure you want to leave the game?")
                        if answer == True:
                            
                            self.leave = True
                        else:
                            self.leave = False
                        
                        if self.leave:
                            pygame.quit()
                    if about_button.collidepoint(event.pos):
                        self.about()
                    if music_button.collidepoint(event.pos):
                        if self.mute_music == False:
                            self.mute_music = True
                        else:
                            self.mute_music = False


            pygame.display.flip()
            
            

    def DisplayBoardWindow(self):
        """
        This function draws most of the writing on the screen.

        :param player: The user
        :type player: string
        """
        run = True
        
        
        while run:
            
            self.DrawGrid()
            
            
            self.SideBar("BoardWindow")
            
            
            pause_button_img = pygame.image.load('imgs/png-transparent-pause-logo-computer-icons-button-media-player-pause-button-rectangle-black-internet-thumbnail.png')
            self.win.blit(pygame.transform.scale(pause_button_img, (50,50)), (850,550))
            
            
                

    def DisplayOpponentsGuesses(self):
        pass
                    
        

    def SideBar(self, screen):
        if screen == "guesses":
            pass
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_button = pygame.Rect(850,550,50,50)
                    pause_button_img = pygame.image.load('imgs/png-transparent-pause-logo-computer-icons-button-media-player-pause-button-rectangle-black-internet-thumbnail.png')
                    self.win.blit(pygame.transform.scale(pause_button_img, (50,50)), (850,550))
                    if pause_button.collidepoint(event.pos):
                        self.Pause_menu()
                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                    
                        rect = pygame.Rect(630, 150, 276, 350)
                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                        for ship in self.ships:
                            ship.draw_ship(self.win)
                        
                    pos = event.pos
                    if event.button == 1:
                        for ship in self.ships:
                            if ship.collide(pos[0], pos[1]):
                                for key,square in self.board.items():
                                    if square[1] == ship.__class__.__name__:
                                        square[1] = ""
                                ship.ship_dragging = True
                                print("hello")
                                if len(self.current_ship) >= 1:
                                    del self.current_ship[0]
                                print(len(self.current_ship))
                                self.current_ship.append(ship)

                                break
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    pos = event.pos
                    x = pos[0]
                    y = pos[1]
                   
                    if event.button == 1:
                        for ship in self.ships:
                            
                            if ship in self.current_ship:
                                ship.ship_dragging = False
                                if ship.rect_1.x > 610 or ship.rect_1.x < 88 or ship.rect_1.y < 50:
                                    ship.reset()
                                    board_bg = pygame.image.load('imgs/board_bg.jpg')
                                    self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                    
                                    rect = pygame.Rect(630, 150, 276, 350)
                                    pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                    ship.draw_ship(self.win)
                                
                                
                                for key,square in self.board.items():
                                    letter_num = key[1]
                                    
                                    
                                        
                                    if square[0].collidepoint(x,y):
                                        if square[1] == "":
                                           
                                                
                                            
                                            if ship.valid_placement(square[0], 0):
                                                if not ship.collide2(square, self.board, key):
                                                    ship.reset()
                                                    board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                    self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                    rect = pygame.Rect(630, 150, 276, 350)
                                                    pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                            
                                                    ship.draw_ship(self.win)
                                                    print("cant put ship there")
                                                else:
                                                   
                                                    
                                                    ship.update_move(square[0].left,square[0].top)
                                                    square[1] = ship.__class__.__name__
                                                    self.index_box.clear()
                                                    
                                                    board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                    self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                    
                                                    rect = pygame.Rect(630, 150, 276, 350)
                                                    pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)

                                            else:
                                                ship.reset()
                                                board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                rect = pygame.Rect(630, 150, 276, 350)
                                                pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                                
                                                ship.draw_ship(self.win)
                                            
                                            
                                        else:
                                            ship.reset()
                                            board_bg = pygame.image.load('imgs/board_bg.jpg')
                                            self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                            rect = pygame.Rect(630, 150, 276, 350)
                                            pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                            
                                            ship.draw_ship(self.win)
                    print(self.board)                
                elif event.type == pygame.MOUSEMOTION:
                    for ship in self.ships:
                        if ship.ship_dragging:
                            pos = event.pos
                            x = pos[0]
                            y = pos[1]
                            
                            print(self.current_ship)
                            if self.current_ship != [None] or len(self.current_ship) != 1:
                                print(self.current_ship)
                                print(x,y)
                                #del self.current_ship[1]
                                board_bg = pygame.image.load('imgs/board_bg.jpg')
                                self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                rect = pygame.Rect(630, 150, 276, 350)
                                pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                self.current_ship[0].update_move(x,y)
                                
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.current_ship[0].change_orientation(self.win)


                
                try:
                    for ship in self.ships:
                        ship.draw_ship(self.win)
                except:
                    pass
                    
                        
                    

            pass
        
        
        

    def DisplayGuessesWindow(self,opp_board):
        run = True
        while run:
            self.DrawGrid()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = event.pos
                    click_pos = print(self.click_grid(mouse, opp_board))
                    for key, value in opp_board.items():
                        if click_pos == key:
                            if value[1] == "Carrier" or value[1] == "Battleship" or value[1] == "Submarine" or value[1] == "Destroyer" or value[1] == "Cruiser":
                                #draw a cross if a ship was hit
                                pass
                            else:
                                
                                #draw circle if not hit a ship
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
        click = False
        #player = bo.start_user
        #bo = n.send("name " + name)
        clock = pygame.time.Clock()
        while starting:
            self.menu_screen()
            starting = False
            break

        board_bg = pygame.image.load('imgs/board_bg.jpg')
        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
        rect = pygame.Rect(630, 150, 276, 350)
        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
        
        while run:
            
            #bo = n.send("get")
            #turn = bo.start_user
            """
            if player.colour == "1":
                self.ships = [Submarine(self.win, 700, 200, "1"), Destroyer(self.win, 710, 210, "1"), Cruiser(self.win, 720, 220, "1"), Battleship(self.win, 730, 230, "1"), Carrier(self.win, 740, 240, "1")]
                
            else:
                self.ships = [Submarine(self.win, 700, 200, "2"), Destroyer(self.win, 710, 210, "2"), Cruiser(self.win, 720, 220, "2"), Battleship(self.win, 730, 230, "2"), Carrier(self.win, 740, 240, "2")]
            """
            pause_button = pygame.Rect(850,550,50,50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            
            self.DisplayBoardWindow()

            #if turn == bo.turn and bo.ready:
            self.DisplayGuessesWindow()
            #else:
            self.DisplayOpponentsGuesses()

            

            
            pygame.display.flip()
            #if bo.player_ready == "False":
                #print("Player not ready")
            
        print("Hello")

        #n.disconnect()



if __name__ == '__main__':
    name = input("Please type your name: ")               
    Game().run(name)
     

