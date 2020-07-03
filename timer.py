import time
import threading
import counter
import winsound

class Timer(counter.Counter):
    
    def __init__(self, hours=0, mins=0, secs=0):
        super().__init__(hours, mins, secs)
        self.can_play_alarm = False
        self.running = False
    
    def start(self):
        self.done = False
        print("Timer Started")
        self.countdown()
    def countdown(self, action = None):
        while not self.is_done():
            
            if action == None:
                self.print_time()
            
            self.decrement()
            time.sleep(1)
        self.timer_done(can_play_alarm=True)
    
    def timer_done(self, can_play_alarm):
        self.done = True
        print("Done")
        
        if can_play_alarm:
            self.play_alarm()
        
        
    def play_alarm(self, length = 2):
        self.can_play_alarm = True
        
        alarm_runtime = time.time() + length
        while time.time() < alarm_runtime and self.can_play_alarm:
            winsound.Beep(500, 200)
            time.sleep(.2)
        
        self.can_play_alarm = False
    
        
        
if __name__ == "__main__":
    timer = Timer(secs=2)
    timer.start()