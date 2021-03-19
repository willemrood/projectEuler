import numpy as np
import functions as func

primes=[1,2]
value = 600851475143
for i in range(3, np.int(np.ceil(np.sqrt(value))) ):
    if value%i==0:
        if func.isprime(i):
            primes.append(i)
print(primes)