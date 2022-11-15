import RPi.GPIO as GPIO
import time
from motortest import start_motor
from tkinter import *
from tkinter import font
import tkinter as tk

flag = True

class Load_sensor():
    def kill_motor(self):
        global flag
        self.dispensing.pack_forget()
        self.hx.power_down()
        flag = False

        return
    
    #, confirmation_screen, win
    def __init__(self, hx, motor_steps, target_val, motor_num):
        global flag
        self.hx = hx
        self.motor_steps = motor_steps
        self.target_val = target_val
        self.motor_num = motor_num
        # self.confirmation_screen = confirmation_screen
        # self.win = win
        # self.dispensing = Frame(self.win)
        # flag = True

        # self.dispensing.pack(fill='both', expand=1)
        # self.confirmation_screen.pack_forget()
        # label = Label(self.dispensing, text='Loading...')
        # label.pack(pady=20)
        # b = tk.Button(self.dispensing, text="CANCEL", command=self.kill_motor).pack()
        # win.update()



    def load_sensor(self):
        # dispensing = Frame(self.win)
        # dispensing.pack(fill='both', expand=1)
        # self.confirmation_screen.pack_forget()
        # label = Label(dispensing, text='Loading...')
        # label.pack(pady=20)
        # b = tk.Button(dispensing, text="CANCEL", command=lambda: self.kill_motor()).pack()
        # print(dispensing.winfo_ismapped())

        global flag

        hx = self.hx
        EMULATE_HX711=False
        referenceUnit = 100
        run_sensors = True

        if not EMULATE_HX711:
            import RPi.GPIO as GPIO
            from hx711 import HX711
        else:
            from emulated_hx711 import HX711

        def cleanAndExit():
            print("Cleaning...")

            if not EMULATE_HX711:
                GPIO.cleanup()

            print("Bye!")
            sys.exit()

        hx.set_reading_format("MSB", "MSB")
        hx.set_reference_unit(referenceUnit)

        hx.reset()
        hx.tare()

        print("Tare done! Add weight now...")

        while flag:
            self.win.update()

            try:       
                val = hx.get_weight(1)
                if val >= self.target_val:
                    self.dispensing.pack_forget()
                    hx.power_down()
                    return
                #steps, out1, out2, out3, out4, ena1, ena2
                if self.motor_num == 1:
                    start_motor(self.motor_steps, 17, 18, 27, 22, 3, 4)
                elif self.motor_num == 2:
                    start_motor(self.motor_steps, 23, 24, 12, 13, 14, 15)
                print(val)

            except (KeyboardInterrupt, SystemExit):
                cleanAndExit()
            
            self.win.update()

        return



# Function to run loadsensor
