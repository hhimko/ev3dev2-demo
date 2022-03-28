#!/usr/bin/env python3
from model import EducatorRobot, GTGController

# define a world of point coordinates for the
# robot to move through
waypoints = [(100,0), (50, 50)]

robot = EducatorRobot()
controller = GTGController(robot)

for wp in waypoints:
    controller.execute(wp)