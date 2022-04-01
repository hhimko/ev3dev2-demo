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
        
    @property
    def _control_variable(self) -> Numeric:
        ''' Calculates the current PID output variable '''
        de = self._vars['derivative']
        E = self._vars['integral']
        e = self._vars['error']
        
        return self.P * e + self.I * E + self.D * de
    
    def reset(self):
        """ Populates PID variables with default values """
        self._vars: Dict[str, Numeric] = {
            'derivative': 0,
            'integral':   0,
            'error':      0
        }
    
    def _on_enter(self):
        self.reset()
    
    def execute(self, error: Numeric):
        self._update_vars(error)
        
        cv = self._control_variable
        self.robot.move(cv)
        
    def _on_exit(self):
        self.robot.stop()
        
    def _update_vars(self, error: Numeric):
        self._vars['integral']  += error
        self._vars['derivative'] = error - self._vars['err_last']
        self._vars['error']      = error