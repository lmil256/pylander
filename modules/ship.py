import math
import pygame
from pygame.locals import *
from pygame.math import *
from modules.gameobject import GameObject

MAX_THRUST = 5
MOON_GRAVITY = -1.62

class Ship(GameObject):
    def __init__(self, position):
        self.position = position
        self.scale = 1
        self.angle = 0
        self.velocity = Vector2()
        self.gravity = Vector2(y=MOON_GRAVITY)
        self.thrust = Vector2()
        self.lines = ((Vector2(-5, 0), Vector2(5, 0)), (Vector2(5, 0), Vector2(0, 15)), (Vector2(0, 15), Vector2(-5, 0)))
        self.flame = Flame(self.position)

    def get_lines(self):
        return tuple((line[0].rotate(self.angle)*self.scale + self.position, \
                      line[1].rotate(self.angle)*self.scale + self.position) for line in self.lines) \
               + self.flame.get_lines()

    def update(self, dt):
        if pygame.key.get_pressed()[K_RIGHT] and not pygame.key.get_pressed()[K_LEFT]:
            self.angle = (self.angle - 45*dt) % 360
            self.flame.angle = (self.angle - 45*dt) % 360
        elif pygame.key.get_pressed()[K_LEFT] and not pygame.key.get_pressed()[K_RIGHT]:
            self.angle = (self.angle + 45*dt) % 360
            self.flame.angle = (self.angle + 45*dt) % 360

        if pygame.key.get_pressed()[K_UP]:
            self.thrust.x = MAX_THRUST*math.cos(math.radians(self.angle+90))
            self.thrust.y = MAX_THRUST*math.sin(math.radians(self.angle+90))
            self.flame.scale = 1
        else:
            self.thrust.x = 0
            self.thrust.y = 0
            self.flame.scale = 0

        acceleration = self.thrust+self.gravity
        self.position += self.velocity*dt + (acceleration * dt**2)/2
        self.flame.position = self.position
        self.velocity += acceleration*dt

        if self.position.y < 0:
            self.position.y = 0
            self.velocity.x = 0
            self.velocity.y = 0

class Flame():
    def __init__(self, position):
        self.position = position
        self.scale = 0
        self.angle = 0
        self.lines = ((Vector2(-4, 0), Vector2(4, 0)), (Vector2(4, 0), Vector2 (0, -10)), (Vector2(0, -10), Vector2(-4, 0))) 

    def get_lines(self):
        if self.scale != 0:
            return tuple((line[0].rotate(self.angle)*self.scale + self.position, \
                          line[1].rotate(self.angle)*self.scale + self.position) for line in self.lines)

        return ()
