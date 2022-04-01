try:
    from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D # type: ignore
except ImportError:
    pass

from model.geometry import Point, Circle
from utils.utils import Numeric, clamp
from bases import Robot


class EducatorRobot(Robot):
    ''' Class wrapper for basic ev3dev2 functionality.
        The whole scripts assumes it's run on a LEGO 
        MINDSTORMS EV3 Educator robot. '''
        
    PULSES_PER_REVOLUTION: Numeric = 360 # wheel encoder pulses per full rotation
    WHEEL_RADIUS: Numeric = 2.6  
    TRACK_WIDTH: Numeric = 12
    
    
    def __init__(self, position: Point, heading_angle: Numeric = 0, speed = 50):
        bounds = Circle(position, radius=self.TRACK_WIDTH/2)
        super().__init__(bounds, heading_angle, speed)
        
        self.drive = MoveSteering(OUTPUT_A, OUTPUT_D)
        
    def move(self, direction: Numeric):
        self.drive.on(clamp(direction, lower=-100, upper=100), self.speed)
        
    def stop(self):
        self.drive.off()