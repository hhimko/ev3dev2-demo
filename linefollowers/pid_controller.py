#!/usr/bin/env python3
from time import sleep

from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.display import Display
from ev3dev2.button import Button

''' PID CONTROL '''
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

    while True:
        CONST_KP = prompt_set_value(CONST_KP, 0.1, "Kp:")
        CONST_KI = prompt_set_value(CONST_KI, 0.1, "Ki:")
        CONST_KD = prompt_set_value(CONST_KD, 0.1, "Kd:")
        DRIVE_SPEED = prompt_set_value(DRIVE_SPEED, 1, "Speed:")
        
        display_print('Press enter to start') 
        button.wait_for_bump(["enter"])
        
        e_prev = E = 0
        while not (button.enter or color.color_name == "Red"):
            process_variable = read_brightness()
            e_curr = set_point - process_variable
            
            E += e_curr # discrete integral term
            e_prim = e_curr - e_prev # derivative term
            e_prev = e_curr
            
            u = CONST_KP * e_curr + CONST_KI * E + CONST_KD * e_prim # PID output 
            drive.on(clamp(u, -100, 100), DRIVE_SPEED)
            
        drive.off()
