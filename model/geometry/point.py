from typing import Tuple, Union
from math import sin, cos


class Vec2:
    """ Basic container structure defining a 2D space coordinate. """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    
    @property
    def coords(self) -> Tuple[float, float]:
        return self.x, self.y
    
    
    def rotated(self, angle: float) -> "Vec2":
        """ Return a new Vec2 object rotated by `angle` radians. """
        _sin, _cos = sin(angle), cos(angle)
         
        nx = self.x * _cos - self.y * _sin
        ny = self.x * _sin + self.y * _cos
        return Vec2(nx, ny)
    
    
    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)
    
    
    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: Union["Vec2", float]) -> "Vec2":
        if isinstance(other, type(self)):
            return Vec2(self.x * other.x, self.y * other.y)
        return Vec2(other * self.x, other * self.y) # type: ignore
    
    
    def __rmul__(self, other: Union["Vec2", float]) -> "Vec2":
        return self.__mul__(other)
    
    
    def __repr__(self):
        return self.__class__.__name__ + "(x={}, y={})".format(self.x, self.y)




class Point(Vec2): # type alias for Vec2
    pass