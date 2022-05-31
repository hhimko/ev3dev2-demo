#!/usr/bin/env python3
from model.robots import EducatorRobot
from model.sensors import DistanceSensor
from controllers import AOController, GTGController
from model.geometry import Point

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3 # type: ignore
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor # type: ignore
from ev3dev2.button import Button # type: ignore


MAX_PROXIMITY_TO_OBSTACLE  = 25.0  
MIN_DISTANCE_FROM_OBSTACLE = 40.0


# instanciate an ev3dev2.Button object to let us control the robot
button = Button()

# define a world of point coordinates for the robot to move through
waypoints = (
    Point(0, -350),
)

# define robot sensors which will be used to measure distance from obstacles
sensors = (
    DistanceSensor(InfraredSensor(INPUT_1), position=Point(7, -7), angle=60),
    DistanceSensor(UltrasonicSensor(INPUT_2), position=Point(7, 0), angle=0),
    DistanceSensor(InfraredSensor(INPUT_3), position=Point(7, 7), angle=-60)
)
weights = (1, 2, 1)

# create a robot, that we'll be controlling
robot = EducatorRobot(speed=50)

STATE_GTG = GTGController(robot)
STATE_AO  = AOController(robot, bias=50, P=100)
current_state = STATE_GTG


curr_waypoint_idx = 0
while curr_waypoint_idx < len(waypoints) and not button.enter:
    print(current_state)

    state = current_state
    with state as controller:
        if current_state == STATE_GTG:
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

        elif current_state == STATE_AO:
            while not button.enter:
                controller.update(sensors, weights)
                
                if min(s.distance for s in sensors) >= MIN_DISTANCE_FROM_OBSTACLE:
                    print("[INFO] Going To Goal")
                    current_state = STATE_GTG
                    break
             