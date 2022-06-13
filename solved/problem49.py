import sys

from    functions import *
import numpy as np
from itertools import permutations
prime_list = []
for i in np.arange(1000,10000):
    if isprime(i):
        prime_list.append(i)

for prime in prime_list:
    prime_str = str(prime)
    prime_list = []
    for prime_perm in permutations(prime_str):
        check_prime = int(prime_perm[0]+prime_perm[1]+prime_perm[2]+prime_perm[3])

        if check_prime>1000:
            if check_prime not in prime_list:
                if isprime(check_prime):
                    prime_list.append(check_prime)
        if len(prime_list)==3:
            print(prime_list)
            print(prime_list[0]-prime_list[1],prime_list[1]-prime_list[2])



