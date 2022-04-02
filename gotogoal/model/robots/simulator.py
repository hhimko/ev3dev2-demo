from math import sin, cos, pi as PI
from typing import Tuple

from model.geometry import Point, Circle
from utils.utils import clamp
from bases import Robot 


class SimulatorRobot(Robot):
    
    PULSES_PER_REVOLUTION: float = 360 # wheel encoder pulses per full rotation
    WHEEL_RADIUS: float = 2.6  
    TRACK_WIDTH: float = 12
    
    def __init__(self, position: Point, heading_angle: float = 0, speed: float = 50):
        super().__init__(Circle(position, radius=1), heading_angle, speed)
        
        
    def move(self, direction: float):
        pow_left, pow_right = self._calc_steering(direction, self.speed)
        
        dist_left, dist_right = self._pow_to_wheel_dist(pow_left, pow_right)
        dist_center = (dist_right + dist_left) / self.TRACK_WIDTH
        
        self.position.x += dist_center * cos(self.angle)
        self.position.y += dist_center * sin(self.angle)
        
        self.angle += (dist_right - dist_left) / self.TRACK_WIDTH
        self.angle %= 360
    
    def stop(self):
        return
    
    @classmethod
    def _pow_to_wheel_dist(cls, pow_left: float, pow_right: float) -> Tuple[float, float]:
        dist_per_unit = 2 * PI * cls.WHEEL_RADIUS / cls.PULSES_PER_REVOLUTION
        return (pow_left * dist_per_unit, pow_right * dist_per_unit)
    
    @staticmethod
    def _calc_steering(direction: float, power: float) -> Tuple[float, float]:
        """ Emulates the ev3dev2.motor.MoveSteering behavior """
        steering = 1 - abs(clamp(direction, lower=-100, upper=100)) / 50
        return (power, power * steering) if direction > 0 else (power * steering, power)