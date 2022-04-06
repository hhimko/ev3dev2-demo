from typing import Dict
from bases import Controller, Robot


class PIDController(Controller):
    ''' Concrete Controller implementation of the PID controller behavior. 
    
            PIDController steers a robot based on a given error value it tries 
        to eliminate. PID 'learns' the enviroment and predicts the next 
        error adjustment in time using integral and differential terms. 
        The most basic PID configuration has the I and D parameters set
        to 0 - then it becomes a Proportional controller.
        
            It's not an easy task to choose the optimal values for the P, I and
        D parameters. The values will vary between every robot and every
        environment, so you should play with them until an optimal behavior 
        is achieved.
        
            For most basic usage, `PID(error)` should be called continuously
        for a desired setpoint SP and a measured process variable PV, where
        `error = SP - PV`. 
        
        You can read more about PID controllers here: 
            https://en.wikipedia.org/wiki/PID_controller '''
            
    def __init__(self, robot: Robot, P: float = 1, I: float = 0, D: float = 0):
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
        ''' Populates PID variables with default values. '''
        
        self._vars = {
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
        self._vars['derivative'] = error - self._vars['error']
        self._vars['error']      = error
        
        
    def execute(self, *args, **kwargs):
        ''' `PIDController.execute()` is forwarded to `PIDController.PID()`.
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call `PIDController.PID()` for clarity. '''
            
        self.PID(*args, **kwargs)
        
    
    def _on_enter(self):
        self.reset()
        
        
    def _on_exit(self):
        self.robot.stop()