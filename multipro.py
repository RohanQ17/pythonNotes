# running tasks on different cpu cores in parallel
# use multi threading for io bound tasks and multi processing for cpu bound tasks,
from multiprocessing import Process, cpu_count
import time

start = time.perf_counter()

def counter(nums):
    count =0
    while(count<nums):
        count +=1

def main():
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))


    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()
    end = time.perf_counter()
    print("finished in ",abs(start-end))




if __name__ == '__main__':
     main()
