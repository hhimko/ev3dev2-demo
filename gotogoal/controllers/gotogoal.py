from utils.collisions import circle_point_collision
from controllers.pid import PIDController
from model.geometry import Point
from bases import Robot


class GTGController(PIDController):
    ''' Concrete Controller implementation of go-to-goal behavior. 
    
        GTGController steers a robot towards a goal defined as a 2D 
        coordinate in space using the PID control system. 
        
        For most basic usage, gotogoal(point) should be called continuously
        on a specific Point object until reached(point) returns True. 
        A robot is said to have reached a particular point, if at the given
        point in time it lays within the boundry box of the robot. '''
    
    def __init__(self, robot: Robot, **kwargs):
        super().__init__(robot, **kwargs)
        
    def reached(self, goal: Point) -> bool:
        ''' Checks whether a Point object lays within the robot's geometry. '''
        return circle_point_collision(self.robot.geometry, goal)
        
    def gotogoal(self, goal: Point):
        super().execute(0)
        
    def execute(self, *args, **kwargs):
        ''' GTGController.execute() is forwarded to GTGController.gotogoal().
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call GTGController.gotogoal() for clarity. '''
            
        self.gotogoal(*args, **kwargs)
        
    def _angle_to_goal(self, goal: Point) -> float:
        return 0
         
    def _on_enter(self):
        return super()._on_enter()
    
    def _on_exit(self):
        return super()._on_exit()