from __future__ import annotations
from utils.utils import Numeric
from math import sqrt


class Point:
    def __init__(self, x: Numeric, y: Numeric):
        self.x = x
        self.y = y
        
    def dist(self, /, other: Point) -> Numeric:
        sx, sy = self.x, self.y
        ox, oy = other.x, other.y
        return sqrt((sx - ox)**2 + (sy - oy)**2)
    
    def __repr__(self):
        return self.__class__.__name__ + f"({self.x}, {self.y})"