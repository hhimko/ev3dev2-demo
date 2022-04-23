from typing import Tuple


class Vec2:
    ''' Basic container structure defining a 2D space coordinate. '''
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    
    @property
    def coords(self) -> Tuple[float, float]:
        return self.x, self.y
    
    
    def __repr__(self):
        return self.__class__.__name__ + "(x={}, y={})".format(self.x, self.y)


class Point(Vec2): # type alias for Vec2
    pass