# from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from model.geometry import Point, Circle
from bases import Robot
from utils import utils

OUTPUT_A: None = None 
OUTPUT_D: None = None
class MoveSteering:
    def __init__(self, *args, **kwargs):
        pass
    def on(self, *args, **kwargs):
        pass
    def off(self):
        pass


class EducatorRobot(Robot):
    ''' Class wrapper for basic ev3dev2 functionality.
        The whole scripts assumes it's run on a LEGO 
        MINDSTORMS EV3 Educator robot. '''
        
    WHEEL_RADIUS = 2.6
    TRACK_WIDTH = 12
    PULSES_PER_REVOLUTION = 360 # wheel encoder pulses per full rotation
    
    
    def __init__(self, pos: Point):
        self.drive = MoveSteering(OUTPUT_A, OUTPUT_D)
        self._geometry = Circle(pos, radius=self.TRACK_WIDTH/2)
        
    def move(self, direction, power):
        self.drive.on(utils.clamp(direction, lower=-100, upper=100), power)
        
    def stop(self):
        self.drive.off()