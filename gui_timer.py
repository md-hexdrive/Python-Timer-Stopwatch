import tkinter as tk
from tkinter import font
from tkinter import ttk

import datetime
import time
import threading

import timer

timer_counter = 0
class Gui_Timer:
    def __init__(self, root = tk.Tk()):
        global timer_counter
        timer_counter += 1
        self.timer_id = timer_counter
        self.my_timer = timer.Timer(mins=2)#, secs = 10)
        
        self.root = root
        self.root.title("Timer " + str(self.timer_id))
        
        # Countdown
        self.countdown_font = font.Font(family='Arial', size=48, weight='bold')
        self.countdown_time = tk.StringVar()
        self.countdown_time.set(self.my_timer.now())
        self.countdown_label = tk.Label(self.root, textvar=self.countdown_time,
                                        font=self.countdown_font, fg='#d65601')
        self.countdown_label.pack(padx=5, pady=5)
        
        # Buttons
        self.button_font = font.Font(family='Arial', size=18, weight='bold')
        
        self.button_frame = tk.Frame(self.root)
        self.start_button = tk.Button(self.button_frame, text="Start/Stop", font=self.button_font,
                                      command=self.start_stop_timer)
        self.reset_button = tk.Button(self.button_frame, text="Reset", font=self.button_font,
                                      command=self.reset_timer)
        self.change_time_button = tk.Button(self.button_frame, text="Change Time",
                                            font=self.button_font)
        self.new_timer_button = tk.Button(self.button_frame, text="+", font=self.button_font,
                                          command=self.create_new_timer)
        
        self.button_frame.pack()
        self.start_button.grid(row=0, column=0, padx=3, pady=5)
        self.reset_button.grid(row=0, column=1, padx=3, pady=5)
        self.change_time_button.grid(row=0, column=2, padx=3, pady=5)
        self.new_timer_button.grid(row=0, column=3, padx=3, pady=5)
        
        self.timer_running = False
        self.root.mainloop()
    
    def start_stop_timer(self):
        if not self.timer_running:
            self.start_timer()
        else:
            self.stop_timer()
    
    def start_timer(self):
        #self.timer_thread = threading.Thread(target=self.my_timer.start)
        
        #self.timer_thread.start()
        self.timer_running = True
        self.root.after(1000, self.update_countdown)
    
    def stop_timer(self):
        print("Stopping timer")
        self.timer_running = False
        #self.my_timer.done = True
    
    def reset_timer(self):
        self.my_timer.reset()
        self.countdown_time.set(self.my_timer.now())
    
    def set_timer_time(self):
        pass
    
    def create_new_timer(self):
        gui_timer = Gui_Timer(self.root)
        
    def update_countdown(self):
        if self.timer_running:
            self.my_timer.decrement()
            self.countdown_time.set(self.my_timer.now())
            if self.my_timer.hours == 0 and self.my_timer.minutes == 0 and self.my_timer.seconds == 0 or self.my_timer.is_done():
                self.timer_running = False
                self.my_timer.timer_done(can_play_alarm=False)
                return
            else:
                self.root.after(1000, self.update_countdown)


if __name__ == "__main__":
    my_gui_timer = Gui_Timer()