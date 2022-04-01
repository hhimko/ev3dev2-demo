from abc import ABC, abstractmethod

from model.geometry import Circle, Point
from utils.utils import Numeric


class Robot(ABC):
    def __init__(self, geometry: Circle, angle: Numeric, speed: Numeric):
        self.geometry = geometry
        self.angle = angle
        self.speed = speed
    
    @property
    def position(self) -> Point:
        return self.geometry.position
    
    @abstractmethod
    def move(self, direction: Numeric):
        pass
    
    @abstractmethod
    def stop(self):
        pass