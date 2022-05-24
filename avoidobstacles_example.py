#!/usr/bin/env python3
from model.robots import EducatorRobot
from model.sensors import DistanceSensor
from controllers import AOController
from model.geometry import Point

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3 # type: ignore
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor # type: ignore
from ev3dev2.button import Button # type: ignore


# instanciate an ev3dev2.Button object to let us control the robot
button = Button()

# define robot sensors which will be used to measure distance from obstacles
sensors = (
    DistanceSensor(InfraredSensor(INPUT_1), position=Point(7, -7), angle=60),
    DistanceSensor(UltrasonicSensor(INPUT_2), position=Point(7, 0), angle=0),
    DistanceSensor(InfraredSensor(INPUT_3), position=Point(7, 7), angle=-60)
)
weights = (1, 2, 1)

# create a robot, that we'll be controlling with an avoid-obstacles controller
robot = EducatorRobot(speed=60)

with AOController(robot, bias=50, P=100) as controller:
     while not button.enter:
        # call AOController.update on each sensor to update the robots heading vector based on sensor readings
        controller.update(sensors, weights)
            
        print(tuple(sensor.distance for sensor in sensors))
        # print("heading: (x={:07.3f}, y={:07.3f})".format(*controller.heading.coords))
    