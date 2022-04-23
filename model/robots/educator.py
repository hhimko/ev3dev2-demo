from math import sin, cos, pi as PI
from typing import Tuple, Optional

try:
    from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D # type: ignore
except ImportError:
    pass

from utils.utils import clamp, radians_normalize
from model.geometry import Point, Circle
from bases import Robot


class EducatorRobot(Robot):
    """ Robot wrapper for basic ev3dev2 functionality.
    
        EducatorRobot assumes it's run on a real LEGO MINDSTORMS EV3 Educator robot. 
    """
        
    PULSES_PER_REVOLUTION = 360 # wheel encoder pulses per full rotation
    WHEEL_RADIUS = 2.6  
    TRACK_WIDTH = 12
    
    def __init__(self, position: Optional[Point]=None, heading_angle: float=0, speed=50):
        if position is None:
            position = Point(0, 0)
        bounds = Circle(position, radius=self.TRACK_WIDTH/2)
        super().__init__(bounds, heading_angle, speed)
        
        self._encoder_readings = (0, 0)
        self._drive = MoveSteering(OUTPUT_A, OUTPUT_D)
        
        
    def update_position(self) -> None:
        dist_left, dist_right = self._get_wheel_dists()
        dist_center = (dist_right + dist_left) / 2
        
        self.position.x += dist_center * cos(self.angle)
        self.position.y += dist_center * sin(self.angle)
        
        self.angle += (dist_right - dist_left) / self.TRACK_WIDTH
        self.angle = radians_normalize(self.angle)
        
        
    def move(self, direction: float) -> None:
        self._drive.on(clamp(direction, lower=-100, upper=100), self.speed)
        
        
    def stop(self) -> None:
        self._drive.off()
        
        
    def _get_wheel_dists(self) -> Tuple[float, float]:
        encoder_left = self._drive.left_motor.position
        encoder_right = self._drive.right_motor.position
        
        left_pulses = encoder_left - self._encoder_readings[0]
        right_pulses = encoder_right - self._encoder_readings[1]
        
        self._encoder_readings = (encoder_left, encoder_right)
        
        dist_per_pulse = 2 * PI * self.WHEEL_RADIUS / self.PULSES_PER_REVOLUTION
        return (left_pulses * dist_per_pulse, right_pulses * dist_per_pulse)