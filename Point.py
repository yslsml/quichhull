import copy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setDirection(self, vector):
        self.direction = vector

    def setSpeed(self, speed):
        self.speed = speed

    def next(self):
        self.x += self.direction.x
        self.y += self.direction.y

    def equals(self, other):
        return self.x == other.x and self.y == other.y
