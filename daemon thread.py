# daemon thread = a thread that runs in background , program will not wait for this thread to get completed
#                 non daemon threads are not normally killed , they stay alive until task is completed
# ex = background tasks, garbage collection etc

import threading
import time

def timer():
    print()
    count =0
    while(True):
        time.sleep(1)
        count+=1
        print("logged in for :",count,"seconds")
x = threading.Thread(target = timer, daemon=True)
x.start()

# using non daemon thread , the timer will not stop as they cannot be killed

answer = input("do you wish to exit  ")
