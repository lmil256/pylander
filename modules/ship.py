import math
import pygame
from pygame.locals import *
from pygame.math import *

MAX_THRUST = 5
ANGLES_PER_SEC = 45
MOON_GRAVITY = -1.62

class Ship():
    def __init__(self, position):
        self.position = position
        self.scale = 1
        self.angle = 90
        self.velocity = Vector2()
        self.gravity = Vector2(y=MOON_GRAVITY)
        self.thrust = Vector2()
        self.lines = ((Vector2(0, 5), Vector2(0, -5)), (Vector2(0, -5), Vector2(15, 0)), (Vector2(15, 0), Vector2(0, 5)))
        self.flame = Flame(self.position)

    def get_lines(self):
        return tuple((line[0].rotate(self.angle)*self.scale + self.position, \
                      line[1].rotate(self.angle)*self.scale + self.position) for line in self.lines) \
               + self.flame.get_lines()

    def update(self, dt):
        rotation = 0

        if pygame.key.get_pressed()[K_LEFT]:
            rotation += ANGLES_PER_SEC*dt
        if pygame.key.get_pressed()[K_RIGHT]:
            rotation -= ANGLES_PER_SEC*dt

        self.angle = (self.angle + rotation) % 360
        self.flame.angle = (self.angle + rotation) % 360

        if pygame.key.get_pressed()[K_UP]:
            self.thrust.x = MAX_THRUST*math.cos(math.radians(self.angle))
            self.thrust.y = MAX_THRUST*math.sin(math.radians(self.angle))
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
        self.lines = ((Vector2(0, 4), Vector2(0, -4)), (Vector2(0, -4), Vector2 (-10, 0)), (Vector2(-10, 0), Vector2(0, 4))) 

    def get_lines(self):
        if self.scale != 0:
            return tuple((line[0].rotate(self.angle)*self.scale + self.position, \
                          line[1].rotate(self.angle)*self.scale + self.position) for line in self.lines)

        return ()
