from __future__ import annotations
from math import sqrt

from utils.utils import Numeric


class Point:
    ''' Simple structure defining a 2D space coordinate. '''
    
    def __init__(self, x: Numeric, y: Numeric):
        self.x = x
        self.y = y
        
    def dist(self, /, other: Point) -> Numeric:
        sx, sy = self.x, self.y
        ox, oy = other.x, other.y
        return sqrt((sx - ox)**2 + (sy - oy)**2)
    
    def __repr__(self):
        return self.__class__.__name__ + f"(x={self.x}, y={self.y})"