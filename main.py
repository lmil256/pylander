import pygame
from pygame.locals import *
from pygame.math import *
import sys
from modules.camera import Camera
from modules.ship import Ship
from modules.level import Level

def main():
    pygame.init()

    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))
    player = Ship(Vector2(0, 0))
    camera = Camera(Vector2(0, 50))
    level = Level()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player.update(dt)

        surface.fill(0x000000)
        camera.draw_thing(surface, level)
        camera.draw_thing(surface, player)

        pygame.display.update()
        dt = clock.tick(60)/1000

main()
