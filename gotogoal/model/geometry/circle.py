from model.geometry import Point


class Circle:
    ''' Basic structure defining a circle in 2D space. '''
    
    def __init__(self, pos: Point, radius: float):
        self.position = pos
        self.radius = radius
        
    @property
    def x(self):
        return self.position.x
    
    @property
    def y(self):
        return self.position.y
    
    def __repr__(self):
        return  self.__class__.__name__ + \
                f"(pos={repr(self.position)}, radius={self.radius})"