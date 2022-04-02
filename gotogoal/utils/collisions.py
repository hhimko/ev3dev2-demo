from math import sqrt

from model.geometry import Circle, Point


def circle_point_collision(c: Circle, p: Point, /) -> bool:
    return circle_point_distance(c, p) <= 0


def point_point_distance(p1: Point, p2: Point, /) -> float:
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def circle_point_distance(c: Circle, p: Point, /) -> float:
    cp = c.position
    return sqrt((cp.x - p.x)**2 + (cp.y - p.y)**2) - c.radius