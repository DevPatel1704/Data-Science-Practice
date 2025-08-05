### multitheading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(num):
    time.sleep(1)
    return f"Number : {num}"

nums = [1,2,3,4,5,6,7,8,0,3,4,1,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,nums)
    
for result in results:
    print(result)