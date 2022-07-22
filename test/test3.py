import pygame
import sys
from pygame.locals import Rect,KEYDOWN,QUIT,K_SPACE

def main():
    pygame.init()
    SURFACE = pygame.display.set_mode((400,300))
    FPSCLOCK = pygame.time.Clock()

    red = pygame.image.load("")    #小さい画像が必要
    red_move = red.get_rect()

    while True:
        #SURFACE.fill((255,255,255))
        #red = pygame.image.load("./画像/ship.png")    
        #red_move = red.get_rect()
        #SURFACE.blit(red,red_move,)
        SURFACE.fill((255,255,255))
        SURFACE.blit(red,red_move,)      
               
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    red_move.move_ip(30,0)
        
        pygame.display.update()
        FPSCLOCK.tick(10)
       

if __name__ == "__main__":
    main()