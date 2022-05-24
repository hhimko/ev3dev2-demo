from typing import Sequence, Optional

from controllers import GTGController
from model.sensors import DistanceSensor
from model.geometry import Vec2


class AOController(GTGController):
    """ Concrete Controller implementation of avoid-bbstacles behavior. 
    
        AOController takes a list of DistanceSensor objects and composes their readings to create
        a 2D space coordinate point, which is in turn used as a heading vector for GTGController.
    """
    def __init__(self, *args, bias: int = 50, **kwargs):
        super().__init__(*args, **kwargs)
        self.heading = Vec2(0, 0)
        self.bias = bias
        
        
    def update(self, sensors: Sequence[DistanceSensor], weights: Optional[Sequence[float]] = None) -> None:
        """ Update the robot heading vector by reading DistanceSensor objects passed as arguments. """
        self._reset_heading()
        if not weights:
            weights = (1 for _ in sensors)
        
        for sensor, w in zip(sensors, weights):
            self.heading += self._get_sensor_vector(sensor) * w
            
        self.heading -= Vec2(self.bias, 0).rotated(self.robot.angle)
            
        super().gotogoal(self.robot.position + self.heading)
        
        
    def execute(self, *args, **kwargs) -> None:
        """ `AOController.execute()` is forwarded to `AOController.update()`.
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call `AOController.update()` for clarity. 
        """
        self.update(*args, **kwargs)
        
        
    def _get_sensor_vector(self, sensor: DistanceSensor) -> Vec2:
        return sensor.get_vector().rotated(self.robot.angle)
        
        
    def _on_enter(self):
        super()._on_enter()
        self._reset_heading()
        
        
    def _reset_heading(self):
        self.heading.x = 0
        self.heading.y = 0