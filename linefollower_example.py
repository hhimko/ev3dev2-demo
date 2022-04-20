#!/usr/bin/env python3
from model.robots import EducatorRobot
from controllers import OnOffController, PIDController

from ev3dev2.sensor.lego import ColorSensor # type: ignore
from ev3dev2.button import Button # type: ignore


# instanciate an ev3dev2.Button object to let us control the robot
button = Button()

# instanciate an ev3dev2.ColorSensor object to read reflected light from below the robot
color = ColorSensor()
color.mode = ColorSensor.MODE_COL_REFLECT

# create a robot, that we'll be controlling with a on-off controller
robot = EducatorRobot(speed=40)

# prompt user to callibrate the set point 
print('Calibrate white.')
button.wait_for_bump( ["enter"] )
white = color.reflected_light_intensity

print('Calibrate black.')
button.wait_for_bump( ["enter"] )
black = color.reflected_light_intensity

set_point = (black + white) / 2


# wrap the robot around a chosen controller class 
with OnOffController(robot, angle=60) as controller:
    # continuously read the sensor and move the robot
    while not (color.color_name == "Red" or button.enter):
        error = set_point - color.reflected_light_intensity
        controller.on_off(error)