from pygame.math import Vector2

class Level():
    def __init__(self):
        self.position = Vector2()
        self.lines = ((Vector2(-1000, 0), Vector2(1000, 0)),)

    def get_lines(self):
        return self.lines
