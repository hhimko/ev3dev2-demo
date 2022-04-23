from math import sqrt

from model.geometry import Circle, Vec2


def circle_point_collision(c: Circle, p: Vec2) -> bool:
    return circle_point_distance(c, p) <= 0


def point_point_distance(p1: Vec2, p2: Vec2) -> float:
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def circle_point_distance(c: Circle, p: Vec2) -> float:
    cp = c.position
    return sqrt((cp.x - p.x)**2 + (cp.y - p.y)**2) - c.radius