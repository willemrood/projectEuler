i=9
from functions import *
import numpy as np
odds = np.arange(1,35103,2)
composites = []
primes = []
for odd in odds:
    if not isprime(odd):
        composites.append(odd)
    else:
        primes.append(odd)

primes=np.array(primes)
composites=np.array(composites)

for comp in composites:
    valid = False
    valid_primes = primes[primes<comp]
    for prime in valid_primes:
        diff = comp-prime
        half_diff = diff/2
        root_half_diff = half_diff**0.5
        if root_half_diff%1==0:
            # print(comp,prime,root_half_diff)
            valid = True
            break
    if not valid:
        print(comp)