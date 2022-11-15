import RPi.GPIO as GPIO
from tkinter import *
from tkinter import font
import tkinter as tk
import time
# from load_sensor_file import load_sensor
from hx711 import HX711
from load_sensor_file import Load_sensor
from manual import run_manual_page
from preset import run_preset_page
import time


def run_main_page(win):
    '''Main program on bootup. From here, user will decide on a manual screen or preset screen.'''

    def change_to_manual():
        manual.pack(fill='both', expand=1)
        preset.pack_forget()
        home_screen.pack_forget()
        run_manual_page(win, manual, keypad, font1)
    def change_to_preset():
        preset.pack(fill='both', expand=1)
        home_screen.pack_forget()
        run_preset_page(win, preset, keypad, font1)


        
    home_screen = Frame(win)
    preset = Frame(win)
    manual = Frame(win) 
    keypad = Frame(win)

    font1 = font.Font(family='Georgia', size='22', weight='bold')
    font2 = font.Font(family='Aerial', size='12')

    label2 = Label(preset, text="this is preset", foreground="blue", font=font2)
    label2.pack(pady=20)
    # Add a button to switch between two frames
    btn1 = Button(home_screen, text="Preset", font=font2, command=change_to_preset)
    btn1.pack(pady=20)
    btn2 = Button(home_screen, text="Manual", font=font2, command=change_to_manual)
    btn2.pack(pady=20)
    home_screen.pack()
    
if __name__ == '__main__':
    run_main_page(win)
    win.mainloop()
