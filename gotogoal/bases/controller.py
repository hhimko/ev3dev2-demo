from abc import ABC, abstractmethod

from bases.robot import Robot


class Controller(ABC):
    def __init__(self, robot: Robot):
        self.robot = robot
    
    @abstractmethod
    def _on_enter(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def _on_exit(self):
        pass
    
    def __enter__(self):
        self._on_enter()
        return self
        
    def __exit__(self, *exc):
        self._on_exit()
        
    def __call__(self, *args, **kwargs):
        self.execute(*args, **kwargs)