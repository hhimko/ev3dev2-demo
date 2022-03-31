#!/usr/bin/env python3
from model.robots import SimulatorRobot, EducatorRobot
from controllers import GTGController
from model.geometry import Point

# define a world of point coordinates for the robot to move through
waypoints = (
    Point(100, 0), Point(50, 50)
)

# create a robot, that we'll be controlling with a go-to-goal controller
robot = SimulatorRobot(position=Point(0,0))

with GTGController(robot) as gotogoal:
    # call GTGController on each waypoint, to drive the robot throught them
    for wp in waypoints:
        gotogoal(wp)
        print(f"waypoint {wp} reached!")