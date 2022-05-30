#!/usr/bin/env python3
from model.robots import EducatorRobot
from model.sensors import DistanceSensor
from controllers import AOController, GTGController
from model.geometry import Point

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3 # type: ignore
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor # type: ignore
from ev3dev2.button import Button # type: ignore


MAX_PROXIMITY_TO_OBSTACLE  = 15.0  
MIN_DISTANCE_FROM_OBSTACLE = 25.0


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


curr_waypoint_idx = 0
while curr_waypoint_idx < len(waypoints):

    with current_state as controller:
        if isinstance(controller, GTGController):
            curr_waypoint = waypoints[curr_waypoint_idx]
            print("[INFO] Moving to {}..".format(curr_waypoint))
            
            while not button.enter:
                controller.gotogoal(curr_waypoint)
                
                if min(s.distance for s in sensors) <= MAX_PROXIMITY_TO_OBSTACLE:
                    print("[INFO] Avoiding Obstacle")
                    current_state = STATE_AO
                    break
                
                if controller.reached(curr_waypoint):
                    print("[INFO] Waypoint successfully reached!\n")
                    curr_waypoint_idx += 1
                    break
            
        elif isinstance(controller, AOController):
            while not button.enter:
                controller.update(sensors, weights)
                
                if min(s.distance for s in sensors) >= MIN_DISTANCE_FROM_OBSTACLE:
                    print("[INFO] Going To Goal")
                    current_state = STATE_GTG
                    break



# with GTGController(robot) as controller:
#     # call GTGController.gotogoal on each waypoint until it's reached by the robot
#     for waypoint in waypoints:
#         print("[INFO] Moving to {}..".format(waypoint))
        
#         while not controller.reached(waypoint):
#             controller.gotogoal(waypoint)
            
#         print("[INFO] Waypoint successfully reached!\n")
