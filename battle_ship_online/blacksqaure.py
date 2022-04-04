import pygame
pygame.init()
SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


coool = True
while coool:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            coool = False
            pygame.quit()
            break

    screen.fill((255,255,255))
    rect1 = pygame.Rect(51,51,50,50)
    pygame.draw.rect(screen, (0,0,0), rect1, 0)
    pygame.display.flip()
     