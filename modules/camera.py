import pygame
from pygame.math import *

class Camera:
    def __init__(self, position):
        self.position = position
        self.canvas_width = 800
        self.canvas_height = 600
        self.zoom = 2

    def get_canvas_width(self):
        return self.canvas_width/self.zoom

    def get_canvas_height(self):
        return self.canvas_height/self.zoom

    def draw_thing(self, surface, thing):
        for line in thing.lines:
            # Convert coordinates to camera space
            line_start = line[0]*thing.scale + thing.position - self.position
            line_end = line[1]*thing.scale + thing.position - self.position
            # Convert coordinates to NDC
            line_start.x = (line_start.x + self.get_canvas_width()/2)/self.get_canvas_width()
            line_start.y = (line_start.y + self.get_canvas_height()/2)/self.get_canvas_height()
            line_end.x = (line_end.x + self.get_canvas_width()/2)/self.get_canvas_width()
            line_end.y = (line_end.y + self.get_canvas_height()/2)/self.get_canvas_height()
            # Convert coordinates to raster space
            line_start.x *= surface.get_width()
            line_start.y = (1-line_start.y)*surface.get_height()
            line_end.x *= surface.get_width()
            line_end.y = (1-line_end.y)*surface.get_height()
            pygame.draw.aaline(surface, 0xffffff, line_start, line_end)
