from typing import Dict
from bases import Controller, Robot


class PIDController(Controller):
    ''' Concrete Controller implementation of the PID controller behavior. '''
    
    def __init__(self, robot: Robot, *, P: float = 1, I: float = 0, D: float = 0):
        super().__init__(robot)
        self.P = P
        self.I = I
        self.D = D
        
        self.reset()
        
    @property
    def _control_variable(self) -> float:
        ''' Calculates the current PID output variable. '''
        de = self._vars['derivative']
        E = self._vars['integral']
        e = self._vars['error']
        
        return self.P * e + self.I * E + self.D * de
    
    def reset(self):
        """ Populates PID variables with default values. """
        self._vars: Dict[str, float] = {
            'derivative': 0,
            'integral':   0,
            'error':      0
        }
        
    def PID(self, error: float):
        self._update_vars(error)
        
        cv = self._control_variable
        self.robot.move(cv)
        
    def _update_vars(self, error: float):
        self._vars['integral']  += error
        self._vars['derivative'] = error - self._vars['err_last']
        self._vars['error']      = error
        
    def execute(self, *args, **kwargs):
        ''' PIDController.execute() is forwarded to PIDController.PID().
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call PIDController.PID() for clarity. '''
            
        self.PID(*args, **kwargs)
    
    def _on_enter(self):
        self.reset()
        
    def _on_exit(self):
        self.robot.stop()