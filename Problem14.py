import numpy as np
import scipy as sp
import pandas as pd
import math
import matplotlib.pyplot as plt
def odd(x):
    return x*3+1
def even(x):
    return  x/2

results = []
for i in range(1,1000000,2):
    run = True
    sequence = []
    n = i
    sequence.append(n)
    while n!=1:
        if n%2 ==0:
            n=even(n)
        else:
            n=odd(n)
        sequence.append(n)
    results.append([i,len(sequence)])
results=np.array(results)
plt.figure()
plt.scatter(results[:,0],results[:,1])
plt.show()