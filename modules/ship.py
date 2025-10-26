import pygame
from pygame.locals import *
from pygame.math import *

class Ship():
    def __init__(self, position):
        self.position = position
        self.scale = 1
        self.velocity = Vector2()
        self.gravity = Vector2(y=-1.62)
        self.thrust = Vector2()
        self.lines = ((Vector2(-5, 0), Vector2(5, 0)), (Vector2(5, 0), Vector2(0, 15)), (Vector2(0, 15), Vector2(-5, 0)))
        self.flame = Flame(self.position)

    def update(self, dt):
        if pygame.key.get_pressed()[K_UP]:
            self.thrust.y = 5
            self.flame.scale = 1
        else:
            self.thrust.y = 0
            self.flame.scale = 0

        acceleration = self.thrust+self.gravity
        self.position += self.velocity*dt + (acceleration * dt**2)/2
        self.flame.position = self.position
        self.velocity += acceleration*dt

        if self.position.y < 0:
            self.position.y = 0
            self.velocity.y = 0

class Flame():
    def __init__(self, position):
        self.lines = ((Vector2(-4, 0), Vector2(4, 0)), (Vector2(4, 0), Vector2 (0, -10)), (Vector2(0, -10), Vector2(-4, 0))) 
        self.scale = 0
