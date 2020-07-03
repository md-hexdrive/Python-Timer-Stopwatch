import datetime
import time
import tkinter as tk
from tkinter import font

import sys

def console_clock():
    tm = datetime.datetime.now()

    print(tm)
    print(get_time())
    print(time.time())
    time.sleep(sync_clock())

    i = 0
    while(i < 60):
        
        print(get_time())
        print(time.time())
        i+=1
        time.sleep(1)

def get_time():
    tm = datetime.datetime.now()
    return tm.strftime("%I:%M:%S %p")

def sync_clock():
    long_time = time.time()
    delay = (int(long_time) + 1) - long_time
    return delay

class Gui_Clock:
    
    def __init__(self, root = tk.Tk()):
        self.root = root
        self.root.title("Clock")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.curr_time = tk.StringVar()
        
        self.curr_time.set(get_time())
        
        self.time_font = font.Font(family='Helvetica', size=24, weight='bold')
        self.time_label = tk.Label(self.frame, textvariable=self.curr_time, font=self.time_font, fg="red")
        
        self.time_label.pack(padx=10, pady=10)
        delay = int(sync_clock() * 1000)
        
        self.root.after(delay, self.update_time)
        self.root.mainloop()
    
    def update_time(self):
        tm = get_time()
        self.curr_time.set(tm)
        print(tm)
        self.root.after(200, self.update_time)
        

if __name__ == "__main__":
    try:
        clock = Gui_Clock()
    except:
        print("An exception occurred")
    #console_clock()
 