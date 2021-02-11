import numpy as np
import matplotlib.pyplot as plt
import time
import os
import math

t0 = time.time()
def divisors(n):
    sum=1
    for i in range(2,int(n/2+1)):
        if n%i==0:
            sum+=i
    return sum
result=[]
for a in range(1,28123):
    for b in range(1,28123):
        c=a+b
        if c<28123:
            if divisors(a)<=a and divisors(b)<=b and c not in result:
                result.append(a)
                continue
                print(a)

print(result)





print(time.time()-t0)