#!/usr/bin/env python3
from controllers import GTGController
from model import EducatorRobot
from model.geometry import Point

# define a world of point coordinates for the
# robot to move through
waypoints = [Point(100,0), Point(50, 50)]

robot = EducatorRobot(pos=Point(0,0))
controller = GTGController(robot)

for wp in waypoints:
    controller.execute()