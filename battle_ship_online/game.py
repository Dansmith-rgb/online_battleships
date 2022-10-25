import ast
import datetime
from pdb import Pdb
import re
import sys
import pygame
from constants import *
from network import Network
import time
from ships import *
import tkinter.messagebox as tk
import tkinter
import json

pygame.init()
class Game():

    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
        pygame.font.init()
        pygame.mixer.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Online battleships")
        self.pos = 0
        self.big_font = pygame.font.SysFont("comicsans", 50)
        self.medium_font = pygame.font.SysFont("comicsans", 30)
        self.small_font = pygame.font.SysFont("comicsans", 20)
        self.boxes = []
        self.ships = [Submarine(self.win, 5, 5, "1"), Destroyer(self.win, 4, 4, "1"), Cruiser(self.win, 720, 220, "1"), Battleship(self.win, 730, 230, "1"), Carrier(self.win, 740, 240, "1", 100, 100)]
        self.current_ship = [None]
        self.index_box = []
        self.mute_music = True # Change back to false 
        self.leave = False
        #self.board = {"A1": ["", "Battleship","1"]}
        self.board = {}
        self.opppsition_board = {}
        self.bo = ""
        self.hit_sound = pygame.mixer.Sound("imgs/hq-explosion-6288.wav")
        self.miss_sound = pygame.mixer.Sound("imgs/splash-by-blaukreuz-6261.wav")
        self.num_of_replays = 0
        
    def menu_screen(self,name):
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
                        self.bo = self.connect()
                        run = False
                        self.run(name)

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
        

        
                

        #pygame.display.flip()  

    def click_grid(self, pos, opp_board):
        x = pos[0]
        y = pos[1]
        for key,square in opp_board.items():
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
            
            

    def DisplayBoardWindow(self, player):
        """
        This function draws most of the writing on the screen.

        :param player: The user
        :type player: string
        """
        run = True
        counter = 0
        total_seconds = 20
        pressed = False
        players_ready = False
        self.win.fill(BLACK)
        if player == "1":
            board = n.send("player 1 ready")
        else:
            board = n.send("player 2 ready")
        
        while pressed == False:
            board = n.send("get")
            
            if board.p1_ready == True and board.p2_ready == True:
                players_ready = True
                pressed=True
            player_waiting = self.big_font.render("Waiting for other player", 1, (0,255,0))
            self.win.blit( player_waiting, (WIDTH / 2 - player_waiting.get_width() / 2, 500))
            pygame.display.flip()
        if players_ready == True:
            
            start_time = datetime.datetime.now()
            end_time = start_time + datetime.timedelta(seconds=30)
            while datetime.datetime.now() < end_time:
                
                
                self.SideBar("BoardWindow", player, run, end_time)
                self.DrawGrid()
                player_placing = self.small_font.render("Place all your ships on the grid", 1, (0,255,0))
                self.win.blit(player_placing, (170, 20))
                
                
                counter += 1
                pause_button_img = pygame.image.load('imgs/png-transparent-pause-logo-computer-icons-button-media-player-pause-button-rectangle-black-internet-thumbnail.png')
                self.win.blit(pygame.transform.scale(pause_button_img, (50,50)), (850,550))
                pygame.display.flip()

    def checkwinner(self,player,board):
        Destroyer = 0
        Submarine = 0
        Carrier = 0
        Cruiser = 0
        Battleship = 0
        if player == "1":
            for ship in self.ships:
                for key,value in board.board_2.items():
                    if value[1] == ship.__class__.__name__:
                        #print(ship.__class__.__name__)
                        if value[2] == "Hit":
                            if ship.__class__.__name__ == "Destroyer":
                                Destroyer += 1
                            elif ship.__class__.__name__ == "Submarine":
                                Submarine += 1
                            elif ship.__class__.__name__ == "Carrier":
                                Carrier += 1
                            elif ship.__class__.__name__ == "Cruiser":
                                Cruiser += 1
                            else:
                                Battleship += 1

            if Destroyer == 2 and Submarine == 3 and Cruiser == 3 and Battleship == 4 and Carrier == 5:
                board = n.send("winner 1")
            else:
                pass
        else:
            for ship in self.ships:
                for key,value in board.board.items():
                    if value[1] == ship.__class__.__name__:
                        #print("wagwan")
                        if value[2] == "Hit":
                            if ship.__class__.__name__ == "Destroyer":
                                Destroyer += 1
                            elif ship.__class__.__name__ == "Submarine":
                                Submarine += 1
                            elif ship.__class__.__name__ == "Carrier":
                                Carrier += 1
                            elif ship.__class__.__name__ == "Cruiser":
                                Cruiser += 1
                            else:
                                Battleship += 1
            if Destroyer == 2 and Submarine == 3 and Cruiser == 3 and Battleship == 4 and Carrier == 5:
                board = n.send("winner 2")
            else:
                pass
        

        
                

    def DisplayOpponentsGuesses(self):
        board_bg = pygame.image.load('imgs/board_bg.jpg')
        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                        
        rect = pygame.Rect(630, 150, 276, 350)
        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
        pause_button_img = pygame.image.load('imgs/png-transparent-pause-logo-computer-icons-button-media-player-pause-button-rectangle-black-internet-thumbnail.png')
        self.win.blit(pygame.transform.scale(pause_button_img, (50,50)), (850,550))
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
        self.DrawGrid()
        player_guessing = self.small_font.render("Oppponent is guessing where your ships are", 1, (0,255,0))
        self.win.blit( player_guessing, (170, 20))
        board = n.send("get")
        
        if player == "1":
            
            
            for key, value in board.board.items():
                if value[2] == "Hit":
                    self.num_of_replays += 1
                    topleft = value[0].topleft
                    bottomright = value[0].bottomright
                    topright = value[0].topright
                    bottomleft = value[0].bottomleft
                    pygame.draw.line(self.win, WHITE, (topleft),(bottomright))
                    pygame.draw.line(self.win, WHITE, (topright),(bottomleft))
                    self.checkwinner(player,board)
                    #print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                             
                            self.hit_sound.play()
                            print("sound opp side 18989090293289378")
                            #print(self.num_of_replays)
                if value[2] == "Miss":
                    self.num_of_replays += 1
                    
                    top = value[0].top
                    bottom = value[0].bottom
                    right = value[0].right
                    left = value[0].left
                    pygame.draw.circle(self.win, WHITE, ((right+left)/2, (top+bottom)/2), 10)
                    #print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.miss_sound.play()
                            print("sound opp side 6475")
                            #print(self.num_of_replays)
                #pygame.time.delay(3000)
                
        else:
            
            for key, value in board.board_2.items():
                if value[2] == "Hit":
                    self.num_of_replays += 1
                    topleft = value[0].topleft
                    bottomright = value[0].bottomright
                    topright = value[0].topright
                    bottomleft = value[0].bottomleft
                    pygame.draw.line(self.win, WHITE, (topleft),(bottomright))
                    pygame.draw.line(self.win, WHITE, (topright),(bottomleft))
                    self.checkwinner(player,board)
                    #print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.hit_sound.play()
                            print("sound opp side 1")
                            #print(self.num_of_replays)
                if value[2] == "Miss":
                    self.num_of_replays += 1
                    top = value[0].top
                    bottom = value[0].bottom
                    right = value[0].right
                    left = value[0].left
                    pygame.draw.circle(self.win, WHITE, ((right+left)/2, (top+bottom)/2), 10)
                    #print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.miss_sound.play()
                            print("sound opp side 2")
                            #print(self.num_of_replays)
                #pygame.time.delay(3000)
                
            
        

    def SideBar(self, screen, player, run, end_time):
        board_bg = pygame.image.load('imgs/board_bg.jpg')
        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                    
        rect = pygame.Rect(630, 150, 276, 350)
        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
        player_waiting = self.medium_font.render(f"{end_time - datetime.datetime.now()}", 1, (0,255,0))
        self.win.blit( player_waiting, (790, 100))
        for ship in self.ships:
            ship.draw_ship(self.win)
        if player == "1":
            
            if screen == "guesses":
                pass
            else:
                board = n.send("get")
                #print(type(board.board))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        return run
                        #pygame.quit()
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
                            player_waiting = self.medium_font.render(f"{end_time - datetime.datetime.now()}", 1, (0,255,0))
                            self.win.blit( player_waiting, (740, 100))
                            for ship in self.ships:
                                ship.draw_ship(self.win)
                            
                        pos = event.pos
                        if event.button == 1:
                            for ship in self.ships:
                                if ship.collide(pos[0], pos[1]):
                                    for key,square in board.board.items():
                                        if square[1] == ship.__class__.__name__:
                                            square[1] = ""
                                            n.send(f"update  {key} 1")
                                            
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
                                
                                if ship in self.current_ship:
                                    ship.ship_dragging = False
                                    if ship.rect_1.x > 610 or ship.rect_1.x < 88 or ship.rect_1.y < 50:
                                        ship.reset()
                                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                        
                                        rect = pygame.Rect(630, 150, 276, 350)
                                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                        ship.draw_ship(self.win)
                                    
                                    
                                    for key,square in board.board.items():
                                        letter_num = key[1]
                                          
                                        if square[0].collidepoint(x,y):
                                            if square[1] == "":
                                            
                                                if ship.valid_placement(square[0], 0):
                                                    #print(key)
                                                    
                                                    if not ship.collide2(square, board, key, n, ship.__class__.__name__, player):
                                                        ship.reset()
                                                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                        rect = pygame.Rect(630, 150, 276, 350)
                                                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                                
                                                        ship.draw_ship(self.win)
                                                        print("cant put ship there")
                                                    else:
                                                        
                                                        ship.update_move(square[0].left,square[0].top)
                                                        #square[1] = ship.__class__.__name__
                                                        
                                                        
                                                        self.index_box.clear()
                                                        
                                                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                        
                                                        rect = pygame.Rect(630, 150, 276, 350)
                                                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                                        player_waiting = self.medium_font.render(f"{end_time - datetime.datetime.now()}", 1, (0,255,0))
                                                        self.win.blit(player_waiting, (740, 100))

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
                                
                    elif event.type == pygame.MOUSEMOTION:
                        for ship in self.ships:
                            if ship.ship_dragging:
                                pos = event.pos
                                x = pos[0]
                                y = pos[1]
                                
                                
                                if self.current_ship != [None] or len(self.current_ship) != 1:
                                    
                                    
                                    self.current_ship[0].update_move(x,y)
                                    
                        
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.current_ship[0].change_orientation(self.win)
                        '''
                        elif event.key == pygame.K_q:
                            
                            run = False
                            return run
                        '''
                    try:
                        for ship in self.ships:
                            ship.draw_ship(self.win)
                    except:
                        pass
                        
                #pass
        else:
            if False:
                pass
                
            else:
                board = n.send("get")
                
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
                                    for key,square in board.board_2.items():
                                        if square[1] == ship.__class__.__name__:
                                            square[1] = ""
                                            n.send(f"update  {key} 2")
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
                                
                                if ship in self.current_ship:
                                    ship.ship_dragging = False
                                    if ship.rect_1.x > 610 or ship.rect_1.x < 88 or ship.rect_1.y < 50:
                                        ship.reset()
                                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                        
                                        rect = pygame.Rect(630, 150, 276, 350)
                                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                        ship.draw_ship(self.win)
                                    
                                    
                                    for key,square in board.board_2.items():
                                        letter_num = key[1]
                                        
                                        
                                            
                                        if square[0].collidepoint(x,y):
                                            if square[1] == "":
                                            
                                                    
                                                
                                                if ship.valid_placement(square[0], 0):
                                                    #board = n.send("update")
                                                    if not ship.collide2(square, board, key, n, ship.__class__.__name__, player):
                                                        ship.reset()
                                                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                        rect = pygame.Rect(630, 150, 276, 350)
                                                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                                
                                                        ship.draw_ship(self.win)
                                                        print("cant put ship there")
                                                    else:
                                                    
                                                        
                                                        ship.update_move(square[0].left,square[0].top)
                                                        #square[1] = ship.__class__.__name__
                                                        # Call to server needed here
                                                        self.index_box.clear()
                                                        
                                                        board_bg = pygame.image.load('imgs/board_bg.jpg')
                                                        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                                        
                                                        rect = pygame.Rect(630, 150, 276, 350)
                                                        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                                        player_waiting = self.medium_font.render(f"{end_time - datetime.datetime.now()}", 1, (0,255,0))
                                                        self.win.blit(player_waiting, (740, 100))
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
                        #print(self.board)                
                    elif event.type == pygame.MOUSEMOTION:
                        for ship in self.ships:
                            if ship.ship_dragging:
                                pos = event.pos
                                x = pos[0]
                                y = pos[1]
                                
                                #print(self.current_ship)
                                if self.current_ship != [None] or len(self.current_ship) != 1:
                                    #print(self.current_ship)
                                    #print(x,y)
                                    #del self.current_ship[1]
                                    #board_bg = pygame.image.load('imgs/board_bg.jpg')
                                    #self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                    #rect = pygame.Rect(630, 150, 276, 350)
                                    #pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                                    self.current_ship[0].update_move(x,y)
                                    
                        
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.current_ship[0].change_orientation(self.win)


                    
                    try:
                        #player_waiting = self.medium_font.render(f"{end_time - datetime.datetime.now()}", 1, (0,255,0))
                        #self.win.blit(player_waiting, (740, 100))
                        for ship in self.ships:
                            ship.draw_ship(self.win)
                        pass
                    except:
                        pass
        
        

    def DisplayGuessesWindow(self,player):
        run = True
        
        opp_board = n.send("get")
        board_bg = pygame.image.load('imgs/board_bg.jpg')
        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
        rect = pygame.Rect(630, 150, 276, 350)
        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
        self.DrawGrid()
        player_guessing = self.small_font.render("It's your turn to guess where the opponents ship may be", 1, (0,255,0))
        self.win.blit( player_guessing, (170, 20))
        pause_button_img = pygame.image.load('imgs/png-transparent-pause-logo-computer-icons-button-media-player-pause-button-rectangle-black-internet-thumbnail.png')
        self.win.blit(pygame.transform.scale(pause_button_img, (50,50)), (850,550))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                n.disconnect()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_button = pygame.Rect(850,550,50,50)
                
                if pause_button.collidepoint(event.pos):
                    self.Pause_menu()
                    board_bg = pygame.image.load('imgs/board_bg.jpg')
                    self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
                                
                    rect = pygame.Rect(630, 150, 276, 350)
                    pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
                #print("RECOGNISED")
                mouse = event.pos
                if player == "1":
                    click_pos = self.click_grid(mouse, opp_board.board_2)
                    #print(click_pos)
                    for key, value in opp_board.board_2.items():
                        if click_pos == key:
                            #print("finally")
                            opp_board = n.send(f"guess {key} {player}")
                else:
                    click_pos = self.click_grid(mouse, opp_board.board)
                    for key, value in opp_board.board.items():
                        if click_pos == key:
                            opp_board = n.send(f"guess {key} {player}")
        if player == "1":
            
            #print("hellooofjdiryuhrzksbtgrkhybsxzlbh")     
            for key, value in opp_board.board_2.items():
                if value[2] == "Hit":
                    self.num_of_replays += 1
                    topleft = value[0].topleft
                    bottomright = value[0].bottomright
                    topright = value[0].topright
                    bottomleft = value[0].bottomleft
                    pygame.draw.line(self.win, WHITE, (topleft),(bottomright))
                    pygame.draw.line(self.win, WHITE, (topright),(bottomleft))
                    print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.hit_sound.play()
                            print("sound232")
                if value[2] == "Miss":
                    self.num_of_replays += 1
                    top = value[0].top
                    bottom = value[0].bottom
                    right = value[0].right
                    left = value[0].left
                    pygame.draw.circle(self.win, WHITE, ((right+left)/2, (top+bottom)/2), 10)
                    print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.miss_sound.play()
                            print("sound!!!!!")
                run = False
        else:
            
            for key, value in opp_board.board.items():
                if value[2] == "Hit":
                    self.num_of_replays += 1
                    topleft = value[0].topleft
                    bottomright = value[0].bottomright
                    topright = value[0].topright
                    bottomleft = value[0].bottomleft
                    pygame.draw.line(self.win, WHITE, (topleft),(bottomright))
                    pygame.draw.line(self.win, WHITE, (topright),(bottomleft))
                    print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.hit_sound.play()
                            print("sound player 2 screen hit")
                if value[2] == "Miss":
                    self.num_of_replays += 1
                    top = value[0].top
                    bottom = value[0].bottom
                    right = value[0].right
                    left = value[0].left
                    pygame.draw.circle(self.win, WHITE, ((right+left)/2, (top+bottom)/2), 10)
                    print(self.num_of_replays)
                    if self.num_of_replays == 1:
                        if not self.mute_music:
                            self.miss_sound.play()
                            print("sound player 2 screen hit")
        
                run = False

                            #else:
                                #root = tkinter.Tk()
                                #root.overrideredirect(1)
                                #root.withdraw()
                                #tk.showerror("Select different box", "You can't choose a box you have already chosen!")
            pygame.display.flip()

    def ending_screen(self,player):
        while True:
            gdata = n.send("get")
            self.win.fill(WHITE)

            
            quit_button = pygame.Rect(400,400,50,50)
            quit_button_img = pygame.image.load('imgs/quit.png')
            self.win.blit(pygame.transform.scale(quit_button_img,(50,50)), (400,400))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    n.disconnect()
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                        break
                    
            
            if player == gdata.winner:
                if player == "1":   
                    player_guessing = self.big_font.render(f"{gdata.p1Name} You won!", 1, (0,255,0))
                    self.win.blit( player_guessing, (300, 50))
                else:
                    player_guessing = self.big_font.render(f"{gdata.p2Name} You won!", 1, (0,255,0))
                    self.win.blit( player_guessing, (300, 50))
            else:
                if player == "1":   
                    player_guessing = self.big_font.render(f"{gdata.p1Name} You lost!", 1, (0,255,0))
                    self.win.blit( player_guessing, (300, 50))
                else:
                    player_guessing = self.big_font.render(f"{gdata.p2Name} You lost!", 1, (0,255,0))
                    self.win.blit( player_guessing, (300, 50))
            """
            if player == "1":   
                player_guessing = self.big_font.render(f"{gdata.p1Name}You won!", 1, (0,255,0))
                self.win.blit( player_guessing, (300, 50))
            else:
                player_guessing = self.big_font.render(f"{gdata.p2Name}You won!", 1, (0,255,0))
                self.win.blit( player_guessing, (300, 50))
            """
            pygame.display.flip()

    def connect(self):
        """
        connect to server function
        """
        global n
        n = Network()
        return n.game_data

    def run(self, name):
        global player
        starting = True
        run = True
        click = False
        player = self.bo.start_user
        game_data = n.send("name " + name)
        clock = pygame.time.Clock()
        #while starting:
            #self.menu_screen()
            #starting = False
            #break
        
        board_bg = pygame.image.load('imgs/board_bg.jpg')
        self.win.blit(pygame.transform.scale(board_bg, (WIDTH,HEIGHT)), (0,0))
        rect = pygame.Rect(630, 150, 276, 350)
        pygame.draw.rect(self.win, WHITE, rect, 0, -1, 20, -1, 20, -1)
        #self.DrawGrid()
        
        self.DisplayBoardWindow(player)
        turn_before = player 
        while run:
            #print("hello")
            gdata = n.send("get")
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            if gdata.winner == "1":
                print(f"Player {gdata.p1Name} won")
            
            if gdata.winner != None:
                if player == "1":
                    self.ending_screen("1")
                else:
                    self.ending_screen("2")
            
            if player == gdata.turn:
                
                if player=="1":
                    if gdata.reset1:
                        self.num_of_replays = 0
                        board = n.send("reset1")
                else:
                    if gdata.reset2:
                        self.num_of_replays = 0
                        board = n.send("reset2")
                self.DisplayGuessesWindow(player)
                turn_before = player
            else:
                
                if player=="1":
                    if gdata.reset1:
                        self.num_of_replays = 0
                        board = n.send("reset1")
                else:
                    if gdata.reset2:
                        self.num_of_replays = 0
                        board = n.send("reset2")
                self.DisplayOpponentsGuesses()
                turn_before = player 
            pygame.display.flip()

            
            
            
            
            """   
            if gdata.winner == "2":
                print(f"Player {gdata.p2Name} won")
                self.ending_screen(gdata.p2Name)
            
            if gdata.winner != None:
                if player == "1":
                    self.ending_screen("1")
                else:
                    self.ending_screen("2")
            """
            
            
            
            
        print("Hello")

        n.disconnect()



if __name__ == '__main__':
    name = input("Please type your name: ")               
    Game().menu_screen(name)
     

