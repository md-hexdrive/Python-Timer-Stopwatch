import time
import counter

def console_chrono():
    countup = counter.Counter()
    print(countup.now())
    print(countup.minutes)
    while countup.minutes < 2:
        countup.increment()
        print(countup.now())
        time.sleep(1)
        
    print("Done")

if __name__ == "__main__":
    console_chrono()