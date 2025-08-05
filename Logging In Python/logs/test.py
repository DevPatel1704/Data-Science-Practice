from logger import logging

def add(a,b):
    
    logging.debug("The addition is tking place")
    return a+b

logging.debug("the addition function is called")
add(3,4)