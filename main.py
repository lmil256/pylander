import pygame
from pygame.locals import *
import sys
from modules.ship import Ship

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    player = Ship(pygame.math.Vector2(WINDOW_WIDTH//2, WINDOW_HEIGHT))
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        surface.fill(pygame.Color(0))

        player.update(dt)
        draw_ship(player, surface)
        pygame.display.update()
        dt = clock.tick(FPS)/1000

def draw_ship(ship, surface):
    for line in ship.lines:
        pygame.draw.aaline(surface, 0xffffff, ship.position+line[0], ship.position+line[1])

main()
