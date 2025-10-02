import pygame
from pygame.locals import *
import sys
from modules.ship import Ship

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))
    player = Ship(WINDOW_WIDTH//2, WINDOW_HEIGHT)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        surface.fill(BLACK)
        surface.fill(WHITE, player)
        player.update(clock.tick(FPS)/1000)
        pygame.display.update()

main()
