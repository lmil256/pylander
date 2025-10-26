from pygame.math import Vector2

class Level():
    def __init__(self):
        self.position = Vector2()
        self.angle = 0
        self.scale = 1
        self.lines = ((Vector2(-1000, 0), Vector2(1000, 0)),)
