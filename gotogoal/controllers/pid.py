from typing import Dict
from bases import Controller, Robot
from utils.utils import Numeric

class PIDController(Controller):
    def __init__(self, robot: Robot, *, P: Numeric = 1, I: Numeric = 0, D: Numeric = 0):
        super().__init__(robot)
        self.P = P
        self.I = I
        self.D = D
        
        self.reset()
        
    def reset(self):
        """ Populates PID variables with default values """
        self._vars: Dict[str, Numeric] = {
            'derivative': 0,
            'integral':   0,
            'err_last':   0
        }
    
    def _on_enter(self):
        self.reset()
    
    def execute(self, error: Numeric):
        self._vars['integral'] += error
        self._vars['derivative'] = error - self._vars['err_last']
        self._vars['err_last'] = error
        
    def _on_exit(self):
        self.robot.stop()