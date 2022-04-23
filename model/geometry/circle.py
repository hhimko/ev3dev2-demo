from model.geometry import Vec2


class Circle:
    ''' Basic structure defining a circle in 2D space. '''
    
    def __init__(self, position: Vec2, radius: float):
        self.position = position
        self.radius = radius
        
        
    @property
    def x(self):
        return self.position.x
    
    
    @property
    def y(self):
        return self.position.y
    
    
    def __repr__(self):
        return  self.__class__.__name__ + \
                "(pos={}, radius={})".format(repr(self.position), self.radius)