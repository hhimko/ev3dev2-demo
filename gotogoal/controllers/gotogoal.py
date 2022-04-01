from controllers.pid import PIDController
from model.geometry import Point
from bases import Robot


class GTGController(PIDController):
    def __init__(self, robot: Robot, **kwargs):
        super().__init__(robot, **kwargs)
        
        
    def _on_enter(self):
        return super()._on_enter()
    
    def execute(self, goal: Point):
        error = self.robot.position.dist(goal)
        super().execute(error)
    
    def _on_exit(self):
        return super()._on_exit()