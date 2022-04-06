#!/usr/bin/env python3
from model.robots import SimulatorRobot, EducatorRobot
from controllers import GTGController
from model.geometry import Point


# define a world of point coordinates for the robot to move through
waypoints = (
    Point(200, 0), Point(125, 100), Point(125, 200)
)

# create a robot, that we'll be controlling with a go-to-goal controller
robot = SimulatorRobot(position=Point(0,0))

with GTGController(robot) as controller:
    # call GTGController.gotogoal on each waypoint until it's reached by the robot
    for waypoint in waypoints:
        print("[INFO] Moving to {}..".format(waypoint))
        
        while not controller.reached(waypoint):
            controller.gotogoal(waypoint)
            
        print("[INFO] Waypoint successfully reached!\n")