import numpy as np
import scipy as sp
import time
t0 = time.time()
run = True
n = 20
number =n
while run:
    for i in range(1,n+1):
        if number%i != 0:
            number +=n
            break
        if i==n:
            run = False
t1 = time.time()
print(number)
print(t1-t0)