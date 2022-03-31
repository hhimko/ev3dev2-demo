from controllers.pid import PIDController
from bases import Robot


class GTGController(PIDController):
    def __init__(self, robot: Robot, **kwargs):
        super().__init__(robot, **kwargs)
        
        
    def _on_enter(self):
        return super()._on_enter()
    
    def _on_exit(self):
        return super()._on_exit()