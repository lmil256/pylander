import pygame
from pygame.locals import *
from pygame.math import *

class Ship():
    def __init__(self, pos):
        self.position = pos
        self.velocity = Vector2()
        self.gravity = Vector2(y=5)
        self.thrust = Vector2()
        self.lines = ((Vector2(-5, 0), Vector2(5, 0)), (Vector2(5, 0), Vector2(0, -15)), (Vector2(0, -15), Vector2(-5, 0)))

    def update(self, dt):
        if pygame.key.get_pressed()[K_UP]:
            self.thrust.y = -10
        else:
            self.thrust.y = 0

        acceleration = self.thrust+self.gravity
        self.position += self.velocity*dt + (acceleration * dt**2)/2
        self.velocity += acceleration*dt

        if self.position.y > 0:
            self.position.y = 0
            self.velocity.y = 0
