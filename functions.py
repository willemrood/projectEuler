import numpy as np
import time

def isprime(x: int):
    run = True
    state = False
    if x == 2 or x == 3:
        run = False
        state = True
    if x%2 == 0 and run:
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
    a = str(x)
    b = a[::-1]
    if a==b:
        state = True
    else:
        state   = False
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
