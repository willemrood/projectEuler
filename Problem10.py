import functions as func
import numpy as np
primes = [2,3]
value = 5
for i in np.arange(5,2000000,2):
    if func.isprime(i):
        primes.append(i)
        value+=float(i)
print(primes)
print(value)