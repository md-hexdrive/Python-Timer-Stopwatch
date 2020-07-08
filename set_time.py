import tkinter as tk
from tkinter import ttk
from tkinter import font
import counter
import gui_timer

class Set_Time(tk.Toplevel):
    def __init__(self, title="Set Time", curr_time="00:40:30"):
        super().__init__()
        self.title(title)
        
        style = ttk.Style(self)
        
        style.configure("mystyle.TButton", highlightthickness=0, bd=0, font=('Arial', 12))
        style.configure("mystyle.TCombobox", font=('Arial', 24))
        style.configure("mystyle.TLabel", font=('Arial', 24))
        #time_font = font.Font(family='Arial', size=48, weight='bold')
        
        self.hours_str = tk.StringVar()
        self.mins_str = tk.StringVar()
        self.secs_str = tk.StringVar()
        
        time_arr = counter.split_time_str(curr_time)
        self.hours_str.set(time_arr[0])
        self.mins_str.set(time_arr[1])
        self.secs_str.set(time_arr[2])
        
        hours_combo = ttk.Combobox(self, width=2, values=tuple(range(0,100)),
                                   textvariable=self.hours_str, font=font.Font(family='Arial', size=24, weight='bold'))
        minutes_combo = ttk.Combobox(self, width=2, values=tuple(range(0,60)),
                                   textvariable=self.mins_str, font=font.Font(family='Arial', size=24, weight='bold'))
        seconds_combo = ttk.Combobox(self, width=2, values=tuple(range(0,60)),
                                   textvariable=self.secs_str, font=font.Font(family='Arial', size=24, weight='bold'))
        
        
        hours_combo.grid(row=1, column=0, padx=5, pady=5)
        minutes_combo.grid(row=1, column=2, padx=5, pady=5)
        seconds_combo.grid(row=1, column=4, padx=5, pady=5)
        
        colon_label = ttk.Label(self, text=":", style="mystyle.TLabel")#, font=time_font)
        colon_label2 = ttk.Label(self, text=":", style="mystyle.TLabel")#, font=time_font)
        colon_label.grid(row=1, column=1, padx=5, pady=5)
        colon_label2.grid(row=1, column=3, padx=5, pady=5)
        
        
        
        set_time_button = ttk.Button(self, text="Set Time", style="mystyle.TButton")#, font=font.Font(family='Arial', size='24'))
        set_time_button.grid(row=2, column=2, columnspan=3, padx=5, pady=5, sticky='e')
    
    def set_time(self):
        return self.hours_str, self.mins_str, self.secs_str

if __name__=='__main__':
    Set_Time()