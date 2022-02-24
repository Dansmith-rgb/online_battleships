import pygame

class Game():

    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 900
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def run(self):
        run = True
        clock = pygame.time.Clock
        while run:
            clock.tick(60)
            f