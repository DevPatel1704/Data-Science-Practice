## processes that run in parallel
## CPU-Bound tasks (E.g Mathematical computation)
## Paraller excecution - multiple core of CPU

import multiprocessing

import time

def sqr_num():
    for i in range(5):
        time.sleep(1)
        print(f"sqr : {i*i}")
        
def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube : {i*i*i}")
        
if __name__ == "__main__":    
    ## create 2 processes

    p1=multiprocessing.Process(target=sqr_num)
    p2=multiprocessing.Process(target=cube_num)
    t=time.time()

    ## Start the process
    p1.start()
    p2.start()

    ## Wait for process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)