from controllers import GTGController
from model.sensors import DistanceSensor
from model.geometry import Vec2


class AOController(GTGController):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heading = Vec2(0, 0)
        
        
    def update(self, sensor: DistanceSensor) -> None:
        pass
        
        
    def execute(self, *args, **kwargs) -> None:
        ''' `AOController.execute()` is forwarded to `AOController.update()`.
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call `AOController.update()` for clarity. 
        '''
        self.update(*args, **kwargs)