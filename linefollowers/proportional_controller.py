#!/usr/bin/env python3
from time import sleep

from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.display import Display
from ev3dev2.button import Button

''' PROPORTIONAL CONTROL '''
DRIVE_SPEED = 67
GAIN_K      = 2.6

drive = MoveSteering(OUTPUT_A, OUTPUT_D)
color = ColorSensor(INPUT_1)
color.mode = ColorSensor.MODE_COL_REFLECT
display = Display()
button = Button()

def clamp(val, _min, _max):
    return min(_max, max(_min, val))

def read_brightness():
    return color.reflected_light_intensity

def display_print(message: str, row=0, clear_screen=True):
    assert 0 <= row < 12
    display.text_pixels(message, clear_screen=clear_screen, y=row*10)
    display.update()
    
def prompt_set_value(val, epsilon, prompt_mess: str):
    def prompt():
        display_print(prompt_mess)
        display_print(str(val), row=1, clear_screen=False)
    
    prompt()
    while True:
        bp = button.buttons_pressed
        if "left" in bp:
            val -= epsilon
            prompt()
        if "right" in bp:
            val += epsilon
            prompt()
        if "enter" in bp:
            return val
        sleep(0.05) # dont let the loop consume 100% of CPU

def calibrateSP():
    display_print('Calibrate white.')
    button.wait_for_bump( ["enter"] )
    white = read_brightness()
    
    display_print('Calibrate black.')
    button.wait_for_bump( ["enter"] )
    black = read_brightness()
    
    return (black + white) / 2
    

if __name__ == "__main__": 
    
    set_point = calibrateSP()
    display_print(str(set_point))
    sleep(2)

    while True:
        GAIN_K = prompt_set_value(GAIN_K, 0.1, "Gain K:")
        DRIVE_SPEED = prompt_set_value(DRIVE_SPEED, 1, "Speed:")
        
        display_print('Press enter to start') 
        button.wait_for_bump(["enter"])

        while not (button.enter or color.color_name == "Red"):
            process_variable = read_brightness()
            error = set_point - process_variable
            
            drive.on(clamp(GAIN_K * error, -100, 100), DRIVE_SPEED)
            
        drive.off()
