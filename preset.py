from tkinter import *
from tkinter import font
import tkinter as tk
from load_sensor_file import Load_sensor
from hx711 import HX711
from keypad_file_test import run_keypad_file
import main_page
import time

AMOUNT = -1
CONTAINER = -1
win = ''


def start_motor_1(container, target_val, confirmation_screen):
    global win
    global pin
    hx = HX711(19, 21)

    # # dispensing = Frame(win)
    # # dispensing.pack(fill='both', expand=1) 
    # for widgets in confirmation_screen.winfo_children():
    #     widgets.destroy()
    # # widgets.after(1000, callback=None)
    # label = Label(confirmation_screen, text='Loading...')
    # label.pack(pady=20)
    # b = tk.Button(confirmation_screen, text="CANCEL", command=lambda: sensor.kill_motor()).pack()
    
    if container == 1:
        # hx, steps, target_val, motor_num
        sensor = Load_sensor(hx, 30, target_val, 1, confirmation_screen, win)
    elif container == 2:
        sensor = Load_sensor(hx, -30, target_val, 1, confirmation_screen, win)
    elif container == 3:
        sensor = Load_sensor(hx, 30, target_val, 2, confirmation_screen, win)
    elif container == 4:
        sensor = Load_sensor(hx, -30, target_val, 2, confirmation_screen, win)
    sensor.load_sensor()

    # dispensing = Frame(win)
    # dispensing.pack(fill='both', expand=1) 
    # for widgets in confirmation_screen.winfo_children():
    #     widgets.destroy()
    # # widgets.after(1000, callback=None)
    # label = Label(confirmation_screen, text='Loading...')
    # label.pack(pady=20)
    # b = tk.Button(confirmation_screen, text="CANCEL", command=lambda: sensor.kill_motor).pack()
    # win.update()


    for widgets in confirmation_screen.winfo_children():
        widgets.destroy()
    label = Label(confirmation_screen, text='Done dispensing ' + str(AMOUNT) + " grams from container " + str(CONTAINER) + "!")
    label.pack(pady=20)
    win.update()
    pin=''
    
    win.after(3000, confirmation_screen.pack_forget)
    win.after(3000, main_page.run_main_page(win))


def run_preset(plist, preset, confirmation_screen):
    global AMOUNT
    global CONTAINER
    CONTAINER = plist[0]
    AMOUNT = plist[1]

    confirmation_screen.pack(fill='both', expand=1)
    preset.pack_forget()
    label = Label(confirmation_screen, text='Are you sure you would like to proceed with ' + str(AMOUNT) +" grams from compartment " + str(CONTAINER) + "?")
    label.pack(pady=20)    
    b = tk.Button(confirmation_screen, text="CONFIRM", command=lambda: start_motor_1(CONTAINER, int(AMOUNT), confirmation_screen)).pack()
    label2 = Label(confirmation_screen, text='Cake Helper will tare once amount is confirmed. Please be patient.')
    label2.pack(pady=20) 


def run_preset_page(window_from_start, preset, keypad, font1):
    global win
    win = window_from_start
    confirmation_screen = Frame(window_from_start)

    label1 = Label(preset, text="Choose a preset", foreground="black", font=font1)
    label1.pack(pady=10)
    btn_start = Button(preset, text="Preset 1", command=lambda: run_preset([2, 20], preset, confirmation_screen))
    btn_start.pack(pady=10)
