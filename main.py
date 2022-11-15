import RPi.GPIO as GPIO
from tkinter import *
from tkinter import font
import tkinter as tk
import time
# from load_sensor_file import load_sensor
from hx711 import HX711
from load_sensor_file import Load_sensor
# from preset import run_preset_page
import time


# import display_choices
# import dispense


# If display_choices ever returns a -1, manual.py will immediately return to main.py, restarting the program.
EXIT = -1
CONTAINER = -1
AMOUNT = -1
pin = ''
confirmation_screen = 'frame'
win = 'window'


def start_motor_1(container, target_val):
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
        sensor = Load_sensor(hx, 30, target_val, 1)
    elif container == 2:
        sensor = Load_sensor(hx, -30, target_val, 1)
    elif container == 3:
        sensor = Load_sensor(hx, 30, target_val, 2)
    elif container == 4:
        sensor = Load_sensor(hx, -30, target_val, 2)
    sensor.load_sensor()


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



def run_main_page(win):
    '''Main program on bootup. From here, user will decide on a manual screen or preset screen.'''

    def change_to_manual():
        manual.pack(fill='both', expand=1)
        home_screen.pack_forget()
        # run_manual_page(win, manual, keypad, font1)
        start_motor_1(1, 20)
    # def change_to_preset():
    #     preset.pack(fill='both', expand=1)
    #     home_screen.pack_forget()
        # run_preset_page(win, preset, keypad, font1)


        
    home_screen = Frame(win)
    preset = Frame(win)
    manual = Frame(win) 
    keypad = Frame(win)

    font1 = font.Font(family='Georgia', size='22', weight='bold')
    font2 = font.Font(family='Aerial', size='12')

    label2 = Label(preset, text="this is preset", foreground="blue", font=font2)
    label2.pack(pady=20)
    # Add a button to switch between two frames
    # btn1 = Button(home_screen, text="Preset", font=font2, command=change_to_preset)
    # btn1.pack(pady=20)
    btn2 = Button(home_screen, text="Manual", font=font2, command=change_to_manual)
    btn2.pack(pady=20)
    home_screen.pack()



    
if __name__ == '__main__':
    win = Tk()
    win.geometry('450x700')
    run_main_page(win)
    win.mainloop()

