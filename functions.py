import numpy as np
import time

def isprime(x):
    run = True
    state = False
    if x==1 or x==2:
        run = False
        state = True
    if x%2==0:
        run = False
        state = False
    if run:
        limit = np.sqrt(x)
        limit = int(np.ceil(limit))
        for i in np.arange(3,limit+1):
            if x%i==0:
                break
            if i == limit:
                state = True
    return state

def ispalindrone(x):
    x = str(x)
    state = False
    run = False
    if len(x)%2 == 0: #if it is even, it runs to check
        run = True
    if run:
        length = len(x)//2
        for i in range(length):
            if x[i] != x[-1-i]: #if leftside is unequal to rightside, break and fail
                break
            if i == length-1: #if it manages to reach the end, it is a palindrone!
                state = True
    return state

def properSum(n):
    divisors = np.arange(2,1+n//2)
    return np.sum(divisors*((n%divisors)==0))

def tictoc(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        functionname = str(func).split()
        print('Function '+functionname[1]+ ' took {} seconds'.format( time.time() - t0))
        return result
    return wrapper

def fibbo(n):
    sequence = []
    if type(n)==int:
        sequence =[1,1]
        for i in range(1,n-1):
            sequence.append( sequence[-2]+sequence[-1])
    if type(n) == list:
        sequence = n
        if len(sequence) >=2:
            sequence.append( sequence[-2]+sequence[-1])
    return sequence
