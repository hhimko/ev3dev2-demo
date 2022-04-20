from bases import Controller, Robot


class OnOffController(Controller):
    ''' Concrete Controller implementation of the On-Off controller behavior. 
    
        OnOffController steers a robot in one angle based on a given error value.
        The direction in which the robot moves is set to either `angle` when the error 
        value passed to `OnOffController.on_off` is positive, and `-angle` otherwise.
    '''
            
    def __init__(self, robot: Robot, angle: float=60):
        super().__init__(robot)
        self.angle = angle
        
        
    def on_off(self, error: float):
        ''' Move the robot in one of the two possible directions based on the error. '''
        direction = (-1 + 2*(error>0)) * self.angle # direction is set to either angle or -angle
        self.robot.move(direction)
        
        
    def execute(self, *args, **kwargs):
        ''' `OnOffController.execute()` is forwarded to `OnOffController.on_off()`.
        
            Unless you need polymorphism between multiple Controller subclasses,
            you should simply call `PIDController.PID()` for clarity. 
        '''    
        self.on_off(*args, **kwargs)
        
        
    def _on_enter(self):
        pass


    def _on_exit(self):
        self.robot.stop()