# Print the current system time continuously in the console, refreshing every second.
# you need to set up a continuous loop that handles three main tasks: 
# 1) fetching the time, 
# 2) clearing the previous output, 
# 3) and pausing.
from datetime import datetime
import time # To use the sleep function

def digital_clock():
    # running an infinite loop using while
    while True:
        # datetime.now() fetches the current date and time, both, when the function runs. 
        now = datetime.now()
        # Gets only time, out of date time in HH:mm:ss format
        current_time = now.strftime("%H:%M:%S")
        # \r -> carriage return, forces cursor to the beginning of output
        # end="" to prevent Python from jumping to a new line
        print(f"\rCurrent Time: {current_time}", end = "", flush = True)
        # Pauses the loop for exactly one second
        time.sleep(1)

digital_clock()