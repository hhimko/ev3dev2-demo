#!/usr/bin/env python3
from model import EducatorRobot

# define a world of point coordinates for the
# robot to move through
waypoints = [(100,0), (50, 50)]

robot = EducatorRobot()

for wp in waypoints:
    robot.gotogoal(wp)