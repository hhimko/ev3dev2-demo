#!/usr/bin/env python3
from model.robots import EducatorRobot
from model.sensors import DistanceSensor
from controllers import AOController, GTGController
from model.geometry import Point

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3 # type: ignore
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor # type: ignore
from ev3dev2.button import Button # type: ignore


# instanciate an ev3dev2.Button object to let us control the robot
button = Button()

# define a world of point coordinates for the robot to move through
waypoints = (
    Point(200, 0), Point(125, 100), Point(125, 200)
)

# define robot sensors which will be used to measure distance from obstacles
sensors = (
    DistanceSensor(InfraredSensor(INPUT_1), position=Point(7, -7), angle=60),
    DistanceSensor(UltrasonicSensor(INPUT_2), position=Point(7, 0), angle=0),
    DistanceSensor(InfraredSensor(INPUT_3), position=Point(7, 7), angle=-60)
)
weights = (1, 2, 1)

# create a robot, that we'll be controlling
robot = EducatorRobot(speed=60)


STATE_GTG = GTGController(robot)
STATE_AO  = AOController(robot, bias=50, P=100)

current_state = STATE_GTG

with current_state as controller:
    while not button.enter:
        if isinstance(controller, AOController):
            # call AOController.update on each sensor to update the robots heading vector based on sensor readings
            controller.update(sensors, weights)
                
            print(tuple(sensor.distance for sensor in sensors))
            # print("heading: (x={:07.3f}, y={:07.3f})".format(*controller.heading.coords))

        elif isinstance(controller, GTGController):


# with GTGController(robot) as controller:
#     # call GTGController.gotogoal on each waypoint until it's reached by the robot
#     for waypoint in waypoints:
#         print("[INFO] Moving to {}..".format(waypoint))
        
#         while not controller.reached(waypoint):
#             controller.gotogoal(waypoint)
            
#         print("[INFO] Waypoint successfully reached!\n")
