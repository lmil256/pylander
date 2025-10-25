import pygame
from pygame.math import *

class Camera:
    def __init__(self, position):
        self.position = position
        self.scale = 1

    def draw_thing(self, surface, thing):
        for line in thing.lines:
            pygame.draw.aaline(surface, 0xffffff,\
                    line[0]*self.scale + thing.position - self.position + Vector2(surface.get_size())/2,
                    line[1]*self.scale + thing.position - self.position + Vector2(surface.get_size())/2)
