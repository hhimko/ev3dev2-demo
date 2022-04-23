from math import atan2, pi as PI

from utils.collisions import circle_point_collision
from utils.utils import radians_normalize
from controllers.pid import PIDController
from model.geometry import Vec2


class GTGController(PIDController):
    ''' Concrete Controller implementation of go-to-goal behavior. 
    
        GTGController steers a robot towards a goal defined as a 2D 
        coordinate in space using the PID control system. 
        
        For most basic usage, `gotogoal(point)` should be called continuously
        on a specific Point object until `reached(point)` returns True. 
        A robot is said to have reached a particular point, if at the given
        point in time it lays within the boundry box of the robot. '''
    
    def __init__(self, *args, P: float=100/PI, **kwargs):
        super().__init__(*args, P=P, **kwargs)
        
        
    def reached(self, goal: Vec2) -> bool:
        ''' Checks whether a Point object lays within the robot's geometry. '''
        
        return circle_point_collision(self.robot.geometry, goal)
        
        
    def gotogoal(self, goal: Vec2) -> None:
        self.robot.update_position()
        
        error = self.robot.angle - self._angle_to_goal(goal)
        super().PID(radians_normalize(error))
        
        
    def execute(self, *args, **kwargs) -> None:
        ''' `GTGController.execute()` is forwarded to `GTGController.gotogoal()`.
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call `GTGController.gotogoal()` for clarity. 
        '''
        self.gotogoal(*args, **kwargs)
        
        
    def _angle_to_goal(self, goal: Vec2) -> float:
        rx, ry = self.robot.position.x, self.robot.position.y
        return atan2(goal.y - ry, goal.x - rx)
