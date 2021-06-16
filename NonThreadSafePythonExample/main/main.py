'''
Created on Jun 16, 2021

@author: nicomp
'''
import threading
import time
import random
from _random import Random

'''
This function will throw an exception when multiple threads try to run .remove() (or .pop() ) on a list BECAUSE it has a logic error.
It's worth studying because the logic error is a good lesson in bad multithreaded programming.
Code in this function was adapted from https://stackoverflow.com/questions/6319207/are-lists-thread-safe
'''
def demoOfNonThreadSafe():
    # Change this number as you please, bigger numbers will get the error quickly
    count = 1000
    l = []
    
    def add():
        for i in range(count):
            l.append(i)
            time.sleep(0.0001)
    
    def remove():
        for i in range(count):
            l.remove(i)     # At some point there will nothing to remove because this thread ran ahead of the other thread.
            time.sleep(0.0001)
    
    
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=remove)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(l)



if __name__ == '__main__':
    demoOfNonThreadSafe()