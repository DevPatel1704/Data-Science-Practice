## Multithreading 
## When to use Multi Threading 
### I/O bound task : tasks that spend more time waitinig for I/O operations (e.g. file operation)
### Concurrent Execution : When you want to imporve the throughput of your application by performing multiple operation concurrently

import threading
import time

def print_number():
    for i in range(5):
        print(f"Number : {i}")
        
def print_letter()