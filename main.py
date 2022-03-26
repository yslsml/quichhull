from Func import *
from math import pi
from Vector import *

def main():
    n = 15
    points = initPoints(n)

    for point in points:  # задаем направление движения точек и скорость
        alfa = random.uniform(0, 2 * pi)  # случайное число с плавающей точкой
        speed = 0.5
        point.setDirection(Vector.getVector(alfa, speed))
        point.setSpeed(speed)

    mainTask(points)

main()