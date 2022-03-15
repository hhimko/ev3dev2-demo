#!/usr/bin/env python3

from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# from ev3dev2.led import Leds
from ev3dev2.display import Display

# REGULATOR DWUSTAWNY

d = Display()
# leds = Leds()


DRIVE_SPEED = 55
DRIVE_ANGLE = 40

drive = MoveSteering(OUTPUT_A, OUTPUT_D)
button = Button()
color = ColorSensor(INPUT_1)


def display_print(message):
    d.clear()
    d.draw.text((0, 0), message)
    d.update()

def calibrate() -> float:
    display_print('Calibrate white')
    button.wait_for_bump(["enter"])
    white = color.hls[1]
    display_print('Calibrate black')
    button.wait_for_bump(["enter"])
    black = color.hls[1]
    return (black + white) / 2
    

# leds.animate_police_lights('RED', 'GREEN') #, sleeptime=0.25)
r = calibrate()
# leds.animate_stop()
# leds.all_off()

display_print('Calibrated, waiting.')
button.wait_for_bump(["enter"])
while not (button.enter or color.color_name == "Red"):
    y = color.hls[1]
    e = r - y
    drive.on((-1 + 2*(e>0)) * DRIVE_ANGLE, DRIVE_SPEED)
    
drive.off()
