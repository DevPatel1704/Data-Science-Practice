## Multithreading 
## When to use Multi Threading 
### I/O bound task : tasks that spend more time waitinig for I/O operations (e.g. file operation)
### Concurrent Execution : When you want to imporve the throughput of your application by performing multiple operation concurrently

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2) ## In here any operations can be happening such as Io operation
        print(f"Number : {i}")
        
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter : {letter}")
        
## Create 2 threads

t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)
 
t=time.time() 

t1.start() 
t2.start()

## Wait for the threads to complete 
t1.join()
t2.join()

# print_number()
# print_letter() 
finished_time=time.time()-t
print(finished_time)    
