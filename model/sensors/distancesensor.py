from typing import Union, Tuple

from model.geometry.point import Vec2

from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor # type: ignore
        

class DistanceSensor:
    def __init__(self, sensor: Union[UltrasonicSensor, InfraredSensor], position: Union[Vec2, Tuple[int, int]], angle: int=0):
        self.sensor = sensor
         
        if isinstance(position, tuple):
            position = Vec2(*position)
        
        self.position = position
        self.angle = angle
        
        
    @property
    def distance(self) -> float:
        """ Get the distance reading from the sensor.
        
            Returns:
                floating point distance in range 0-70cm 
        """
        if isinstance(self.sensor, UltrasonicSensor):
            # UltrasonicSensor has a much broader range than InfraredSensor, so the reading is truncated 
            return min(self.sensor.distance_centimeters, 70) 
        return self.sensor.proximity * 0.70 # proximity returns a percentage of its max distance, equal to 70cm
    
    
    @property
    def distance_norm(self) -> float:
        """ Return the distance read by the sensor, normalized to the [0, 1] range. """
        return self.distance / 70
    