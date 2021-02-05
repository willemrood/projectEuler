import numpy as np
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


