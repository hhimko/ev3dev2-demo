#!/usr/bin/env python3
from datetime import datetime
from time import sleep
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# from ev3dev2.led import Leds
from ev3dev2.display import Display

# REGULATOR PROPORCJONALNY

d = Display()
# leds = Leds()


DRIVE_SPEED = 50
CONST_K = 2

drive = MoveSteering(OUTPUT_A, OUTPUT_D)
button = Button()
color = ColorSensor(INPUT_1)

def clamp(x, _min, _max) -> float:
    return min(_max, max(_min, x))

def display_print(message):
    d.clear()
    d.draw.text((0, 0), message)
    d.update()

def choose_k(start_k):
    display_print(str(start_k))
    while not button.enter:
        b = button.buttons_pressed
        if "left" in b:
            start_k -= 0.1
            display_print(str(start_k))
            # display_print(f'Current K = {str(start_k)}')
            sleep(0.05)
        elif "right" in b:
            start_k += 0.1
            display_print(str(start_k))
            # display_print(f'Current K = {str(start_k)}')
            sleep(0.05)
    return start_k

def choose_speed(start_speed):
    display_print(str(start_speed))
    while not button.enter:
        b = button.buttons_pressed
        if "left" in b:
            start_speed -= 0.5
            display_print(str(start_speed))
            # display_print(f'Current K = {str(start_k)}')
            sleep(0.05)
        elif "right" in b:
            start_speed += 0.5
            display_print(str(start_speed))
            # display_print(f'Current K = {str(start_k)}')
            sleep(0.05)
    return start_speed
    

def calibrate() -> float:
    display_print('Calibrate white')
    button.wait_for_bump(["enter"])
    white = color.hls[1]
    display_print('Calibrate black')
    button.wait_for_bump(["enter"])
    black = color.hls[1]
    return (black + white) / 2
    

# leds.animate_police_lights('RED', 'GREEN') #, sleeptime=0.25)

# leds.animate_stop()
# leds.all_off()

r = calibrate()  # TODO add optional calibration values print
display_print(str(r))
sleep(2)

def program():
    global CONST_K
    global DRIVE_SPEED
    CONST_K = choose_k(CONST_K)
    sleep(0.5)
    DRIVE_SPEED = choose_speed(DRIVE_SPEED)
    display_print('Calibrated, waiting.')
    button.wait_for_bump(["enter"])

    while not (button.enter or color.color_name == "Red"):
        y = color.hls[1]
        e = r - y
        drive.on(clamp(CONST_K * e, -100, 100), DRIVE_SPEED)
        
    drive.off()

while True:
    start = datetime.now()
    program()
    end = datetime.now()
    msg = 'Time: ' + str(end-start)
    display_print(msg)
    sleep(3)

# last: K = 1.8, Speed = 55, Time = 
