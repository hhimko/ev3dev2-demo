from abc import ABC, abstractmethod

from bases.robot import Robot
from gotogoal.controllers.pid import PIDController


class Controller(ABC):
    ''' Abstract Controller class. '''
    
    def __init__(self, robot: Robot):
        self.robot = robot
    
    @abstractmethod
    def _on_enter(self):
        pass
    
    @abstractmethod
    def execute(self):
        ''' Alias for the main function of a particular Controller implementation,
            e.g. PIDController.execute() is simply forwarded to PIDController.PID().
            Controller.execute() provides a naming compability for all controllers. '''
        pass
    
    @abstractmethod
    def _on_exit(self):
        pass
    
    def __enter__(self):
        ''' Most Controller subclasses naturally require a setup/teardown funtionality,
            hence a context manager protocol is used in all controller implementations. '''
        self._on_enter()
        return self
        
    def __exit__(self, *exception_handlers):
        self._on_exit()