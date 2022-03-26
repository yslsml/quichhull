import matplotlib.pyplot as plt
from math import *
import random
from Point import Point
from Vector import Vector


def initPoints(n) -> list:
    X = [random.randint(0, 10) for _ in range(n)]
    Y = [random.randint(0, 10) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i])
        for j in range(len(points)):
            if el.equals(points[j]):
                el.x = random.randint(0, 10)
                el.y = random.randint(0, 10)
        points.append(el)
    return points


def determinant(p, p1, p2):  # p относительно p1p2
    return (p2.x - p1.x) * (p.y - p1.y) - (p.x - p1.x) * (p2.y - p1.y)


def drawPolygon(points: list):
    for i in range(0, len(points)):
      if i + 1 == len(points):
        k = 0  # k - индекс последней точки
      else:
        k = i + 1
      plt.plot([points[i].x, points[k].x], [points[i].y, points[k].y], color="orange")


def drawPoints(points):
    n = len(points)
    for i in range(n):
        plt.scatter(points[i].x, points[i].y)  # рисует точку


def area(p1, p2, p3):
    return abs(determinant(p3, p1, p2))


def distance(p1, p2):
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))


def findMinPoint(points):
    n = len(points)
    min = points[0]
    for i in range(1, n):
        if min.x > points[i].x:
            min = points[i]
    return min


def findMaxPoint(points):
    n = len(points)
    max = points[0]
    for i in range(1, n):
        if points[i].x > max.x:
            max = points[i]
    return max


def findLeftSet(points, p1, p2):
    leftSet = []
    for i in range(len(points)):
        if determinant(points[i], p1, p2) > 0:  # left
            leftSet.append(points[i])
    return leftSet


def findRightSet(points, p1, p2):
    rightSet = []
    for i in range(len(points)):
        if determinant(points[i], p1, p2) < 0:  # right
            rightSet.append(points[i])
    return rightSet


def findFurthestPoint(points, leftPoint, rightPoint):
    maxArea = area(leftPoint, rightPoint, points[0])
    furthestPoint = points[0]
    for i in range(1, len(points)):
        if area(leftPoint, rightPoint, points[i]) > maxArea:
            maxArea = area(leftPoint, rightPoint, points[i])
            furthestPoint = points[i]
    return furthestPoint


def findHull(leftPoint, rightPoint, points, hull):
    furthestPoint = findFurthestPoint(points, leftPoint, rightPoint)

    leftSubset = findLeftSet(points, leftPoint, furthestPoint)
    rightSubset = findLeftSet(points, furthestPoint, rightPoint)

    if leftSubset:
        findHull(leftPoint, furthestPoint, leftSubset, hull)
        hull.append(furthestPoint)
    else:
        hull.append(furthestPoint)

    if rightSubset:
        findHull(furthestPoint, rightPoint, rightSubset, hull)
    else:
        hull.append(furthestPoint)


def quickHull(points):
    hull = []
    leftPoint = findMinPoint(points)
    rightPoint = findMaxPoint(points)

    leftSet = findLeftSet(points, leftPoint, rightPoint)
    rightSet = findRightSet(points, leftPoint, rightPoint)

    hull.append(leftPoint)
    findHull(leftPoint, rightPoint, leftSet, hull)  # ищем оболочку верхнего множества
    hull.append(rightPoint)
    findHull(rightPoint, leftPoint, rightSet, hull)  # ищем оболочку нижнего множества

    hull.append(hull[0])
    return hull


def findPerimeter(hull):
    k = len(hull)
    sum = 0
    for i in range(0, k):
        sum += distance(hull[i], hull[(i+1) % k])
    return sum


def mainTask(points):
    plt.ion()  # включение интерактивного режима для анимации

    time = 30
    hull = quickHull(points)
    MAX_P = findPerimeter(hull) + 5

    while time:
        plt.clf()  # очистить текущую фигуру
        drawPoints(points)
        hull = quickHull(points)
        drawPolygon(hull)
        perimeter = findPerimeter(hull)
        if perimeter > MAX_P:
            for p in points:
                scalar = -1
                tmpVector = Vector.multiplyOnScalar(p.direction, scalar)
                p.setDirection(tmpVector)
        for p in points:
            p.next()  # точка движется дальше по направлению

        plt.draw()
        plt.gcf().canvas.flush_events()
        plt.pause(0.0001)
        time -= 1

    plt.ioff()  # выключение интерактивного режима
    plt.show()









