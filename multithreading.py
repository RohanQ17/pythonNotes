#  thread = a flow of execution.like a separate order of instructions.
#             however each thread takes a turn running to achieve concurrency
#           GIL =(global interpreter lock) allows only one thread to hold the control of python interpreter

#cpu bound = program spends most of its time waiting for internal events (cpu intensive)
# io bound = program spends most of its time waiting for external events like user input or web scraping
# as multithreading

import threading
import time


def run():
    time.sleep(4)
    print("running task is done")

def fidgeting():
    time.sleep(2)
    print("fidgeted")

def go():
    time.sleep(4)
    print("its time")


x = threading.Thread(target=run, args=())
x.start()
y = threading.Thread(target=fidgeting, args=())          # runs concurrently now instead of sequentially
y.start()
z = threading.Thread(target=go, args=())
z.start()

x.join()
y.join()
z.join()  # now main thread will wait for these threads to get over and join with it before it can perform its own tasks
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())



