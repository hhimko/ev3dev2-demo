from typing import Union, Tuple
from math import sin, cos, radians, degrees

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
    def angle(self) -> float:
        return degrees(self._angle)
    
    
    @angle.setter
    def angle(self, value: float) -> None:
        self._angle = radians(value)
        
        
    @property
    def angle_rad(self) -> float:
        return self._angle
    
    
    @angle_rad.setter
    def angle_rad(self, value: float) -> None:
        self._angle = value
        
        
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
    
    
    def get_vector(self, normalize: bool = False) -> Vec2:
        """ Return a new vector from the current distance reading. """
        dist = self.distance_norm if normalize else self.distance
        return self.position + Vec2(dist * cos(self.angle_rad), dist * sin(self.angle_rad))
    