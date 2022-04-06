class Point:
    ''' Basic container structure defining a 2D space coordinate. '''
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    
    def __repr__(self):
        return self.__class__.__name__ + "(x={}, y={})".format(self.x, self.y)