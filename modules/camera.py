import pygame
from pygame.math import *

class Camera:
    def __init__(self, position):
        self.position = position
        self.canvas_width = 200
        self.canvas_height = 150
        self.zoom = 1

    def draw_thing(self, surface, thing):
        for line in thing.lines:
            # Convert coordinates to camera space
            line_start = line[0]+thing.position-self.position
            line_end = line[1]+thing.position-self.position
            # Convert coordinates to NDC
            line_start.x = (line_start.x + self.canvas_width/2)/self.canvas_width
            line_start.y = (line_start.y + self.canvas_height/2)/self.canvas_height
            line_end.x = (line_end.x + self.canvas_width/2)/self.canvas_width
            line_end.y = (line_end.y + self.canvas_height/2)/self.canvas_height
            # Convert coordinates to raster space
            line_start.x *= surface.get_width()
            line_start.y = (1-line_start.y)*surface.get_height()
            line_end.x *= surface.get_width()
            line_end.y = (1-line_end.y)*surface.get_height()
            pygame.draw.aaline(surface, 0xffffff, line_start, line_end)
