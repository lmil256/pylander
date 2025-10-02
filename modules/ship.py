import pygame
from pygame.locals import *

class Ship(pygame.Rect):
    def __init__(self, start_x, start_y):
        super().__init__(0, 0, 10, 20)
        self.centerx = start_x
        self.bottom = start_y
        self.velocity = 0.0
        self.acceleration = 2.0 
        self.position = float(start_y)

    def update(self, dt):
        if pygame.key.get_pressed()[K_UP]:
            self.acceleration = -5
        else:
            self.acceleration = 2
        self.position += self.velocity*dt + (self.acceleration * dt**2)/2
        self.velocity += self.acceleration*dt
        self.bottom = self.position
        if self.position > 600:
            self.position = 600.0
            self.velocity = 0
