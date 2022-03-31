#!/usr/bin/env python3
from model.robots import EducatorRobot
from controllers import GTGController
from model.geometry import Point

# define a world of point coordinates for the robot to move through
waypoints = (
    Point(100, 0), Point(50, 50)
)

robot = EducatorRobot(position=Point(0,0), heading_angle=0)
controller = GTGController(robot)

for wp in waypoints:
    controller.execute()