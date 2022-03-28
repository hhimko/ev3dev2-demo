from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from scripts import utils

class EducatorRobot:
    ''' Class wrapper for basic ev3dev2 functionality.
        The whole scripts assumes it's run on a LEGO 
        MINDSTORMS EV3 Educator robot. '''
        
    WHEEL_RADIUS = 1.0
    TRACK_WIDTH = 1.0
    
    
    def __init__(self):
        self.drive = MoveSteering(OUTPUT_A, OUTPUT_D)
        
    def move(self, direction, power):
        self.drive.on(utils.clamp(direction, lower=-100, upper=100), power)
        
    def stop(self):
        self.drive.off()