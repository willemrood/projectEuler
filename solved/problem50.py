from functions import *
import numpy as np
primes = []
limit = 1000000
for i in range(limit):
    if isprime(i):
        primes.append(i)
n = len(primes)
primes = np.array(primes)
print(primes)
consec_sum = primes
for i in range(n):
    consec_sum = consec_sum[:-1]+primes[1+i:]
    check_sum = consec_sum[consec_sum<limit]
    for p in check_sum:
        if isprime(p):
            print(p,i+2)

