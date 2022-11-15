from tkinter import *
from tkinter import font
import tkinter as tk
from load_sensor_file import Load_sensor
from hx711 import HX711
from keypad_file_test import run_keypad_file
import main_page
import time

# If display_choices ever returns a -1, manual.py will immediately return to main.py, restarting the program.
EXIT = -1
CONTAINER = -1
AMOUNT = -1
pin = ''
confirmation_screen = 'frame'
win = 'window'


def start_motor_1(container, target_val, confirmation_screen):
    global win
    global pin
    hx = HX711(19, 21)

    
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


    for widgets in confirmation_screen.winfo_children():
        widgets.destroy()
    label = Label(confirmation_screen, text='Done dispensing ' + str(AMOUNT) + " grams from container " + str(CONTAINER) + "!")
    label.pack(pady=20)
    win.update()
    pin=''
    
    win.after(3000, confirmation_screen.pack_forget)
    win.after(3000, main_page.run_main_page(win))

def load_confirmation_screen(keypad):
    '''Kills keypad window and loads confirmation screen window.'''
    global confirmation_screen
    confirmation_screen.pack(fill='both', expand=1)
    keypad.pack_forget()
    label = Label(confirmation_screen, text='Are you sure you would like to proceed with ' + str(AMOUNT) +" grams from compartment " + str(CONTAINER) + "?")
    label.pack(pady=20)    
    b = tk.Button(confirmation_screen, text="CONFIRM", command=lambda: start_motor_1(CONTAINER, int(AMOUNT), confirmation_screen)).pack()
    label2 = Label(confirmation_screen, text='Cake Helper will tare once amount is confirmed. Please be patient.')
    label2.pack(pady=20) 


def create_buttons(value, keys, keypad, e):
    '''Acts on button inputs. If user hits "=", saves value as AMOUNT and runs loads confirmation screen and ends function.'''
    # inform function to use external/global variable
    global pin
    global AMOUNT
    def add_label(e):
        Label(keypad, text=e.char).pack()
    if value == '-':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)
    elif value == '=':
        AMOUNT = pin
        load_confirmation_screen(keypad)
        return
        # print("pin is " + str(AMOUNT))

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e.insert('end', value)
    
    for x in range(4):
        for y in range(3):
            keypad.bind(keys[x][y], add_label)
# --- main ---

def wipe_container_and_call_numpad(manual, keypad):
    '''Create buttons through keypad window. When buttons are clicked, they run create_buttons fucntion.'''
    keypad.pack(fill='both', expand=1)
    manual.pack_forget()

    keys = [
        ['1', '2', '3'],    
        ['4', '5', '6'],    
        ['7', '8', '9'],    
        ['-', '0', '='],
    ]

    # place to display pin
    e = tk.Entry(keypad)
    e.grid(row=0, column=0, columnspan=4, ipady=5)

    # create buttons using `keys`
    for y, row in enumerate(keys, 1):
        for x, key in enumerate(row):
            b = tk.Button(keypad, text=key, command=lambda val=key:create_buttons(val, keys, keypad, e))
            b.grid(row=y, column=x, ipadx=10, ipady=10)

def set_container(container_num, manual, keypad):
    '''Set CONTAINER as container_num and open numpad'''
    global CONTAINER
    CONTAINER = container_num
    wipe_container_and_call_numpad(manual, keypad)


def run_manual_page(window_from_start, manual, keypad, font1):
    global confirmation_screen
    global win
    win = window_from_start

    confirmation_screen = Frame(win)
    label1 = Label(manual, text="Choose a container", foreground="black", font=font1)
    label1.pack(pady=10)
    btn_start = Button(manual, text="Container 1", command=lambda: set_container(1, manual, keypad))
    btn_start.pack(pady=10)
    btn_start = Button(manual, text="Container 2", command=lambda: set_container(2, manual, keypad))
    btn_start.pack(pady=10)
    btn_start = Button(manual, text="Container 3", command=lambda: set_container(3, manual, keypad))
    btn_start.pack(pady=10)
    btn_start = Button(manual, text="Container 4", command=lambda: set_container(4, manual, keypad))
    btn_start.pack(pady=10)
