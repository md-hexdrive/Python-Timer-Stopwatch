import datetime
import time

"""
TODO: check times to ensure they are properly formatted (i.e., no minutes or seconds > 59)
TODO: determine what happens when hours > 99
TODO: implement time incrementing
TODO: implement time decrementing

TODO: Throw an exception, or otherwise properly inform the user when the countdown is complete

TODO: implement proper timing code (using time.sleep() or the datetime library or time.time)

TODO: add alarms to the program
TODO: allow the user to tell the program to perform a user-defined action (run a program, call a function, etc.) when at specific timer/alarm is done (or even reaches a certain point in time)

"""
class Counter:
    def __init__(self, hrs = 0, mins = 0, secs = 0):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs
        self.done = False
        
        self.start_time = (hrs, mins, secs)
    
    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.mins = minutes
        self.secs = seconds
        self.done = False
    
    def is_done(self):
        return self.done
    
    def now(self):
        return FormatTime(self.hours, self.minutes, self.seconds).format_time()
    
    def __str__(self):
        return self.now()
    
    def increment(self):
        if self.seconds >= 0 and self.seconds <= 59:
            self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        
    
    def decrement(self):
        if self.is_done():
            print("We are done, you can't decrement any further")
            return
        if self.seconds >= 0:
            self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes < 0:
            self.minutes = 59
            self.hours -= 1
        
        if self.hours < 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.done = True
        #if self.seconds == 0 and self.minutes > 0 or self.hours > 0:
    
    def reset(self):
        self.done = False
        self.hours, self.minutes, self.seconds = self.start_time
    def print_time(self):
        print(self.now())
        
class FormatTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    
    def format_time(self):
        hr_str = ""
        min_str = ""
        sec_str = ""
        
        if (self.hours < 10):
            hr_str = str(0)
        hr_str += str(self.hours)
        
        if self.minutes < 10:
            min_str += str(0)
        min_str += str(self.minutes)
        
        if self.seconds < 10:
            sec_str += str(0)
        sec_str += str(self.seconds)
        return hr_str + ":" + min_str + ":" + sec_str

if __name__ == "__main__":
    counter = Counter(3, 59, 50)
    print(counter.now())
    
    for i in range(20):
        counter.increment()
        print(counter.now())
    
    counter.reset()
    print("Timer Reset: ", counter.now())
