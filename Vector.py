from math import *
from Point import Point

class Vector:
    def __init__(self, point1, point2):
        if type(point1) == Point:
            self.x = point2.x - point1.x
            self.y = point2.y - point1.y
        else:
            self.x = point1
            self.y = point2

    @staticmethod
    def getVector(alpha, speed=1):
        return Vector(speed * cos(alpha), speed * sin(alpha))  # возвращаем вектор (направление)

    @staticmethod
    def multiplyOnScalar(v, scalar):
        vector = Vector(v.x * scalar, v.y * scalar)
        return vector


