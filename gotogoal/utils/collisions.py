from model.geometry import Circle, Point


def circle_point_collision(c: Circle, p: Point) -> bool:
    return p.dist(c.position) <= c.radius