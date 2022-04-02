from abc import ABC, abstractmethod

from model.geometry import Circle, Point


class Robot(ABC):
    ''' Abstract Robot class. '''
    
    def __init__(self, geometry: Circle, angle: float, speed: float):
        self.geometry = geometry
        self.angle = angle
        self.speed = speed
    
    @property
    def position(self) -> Point:
        return self.geometry.position
    
    @abstractmethod
    def move(self, direction: float):
        pass
    
    @abstractmethod
    def stop(self):
        pass