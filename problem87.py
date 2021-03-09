from functions import *
import numpy as np
from itertools import combinations,permutations
lim = 50e6
soft_limit = lim**(1/2)
primes = []
for p in np.arange(np.ceil(soft_limit)):
    if isprime(int(p)):
        primes.append(p)
primes = np.array(primes)
primes_s = primes**2
primes_c = primes**3
primes_q = primes**4
primes_c = primes_c[primes_c<lim]
primes_q = primes_q[primes_q<lim]

valid_numbers=[]
for i in primes_s:
    for j in primes_c:
        for k in primes_q:
            sum = i+j+k
            if sum<lim:
                valid_numbers.append(sum)
valid_numbers = np.array(valid_numbers)
valid_numbers = np.unique(valid_numbers)
print(valid_numbers)
print(len(valid_numbers))