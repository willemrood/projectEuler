import sys

from    functions import *
import numpy as np
from itertools import combinations, combinations_with_replacement
prime_list = []
for i in range(4000):
    if isprime(i):
        prime_list.append(i)

distinctions = 3
offset = distinctions-1
combos = np.array(list(combinations(prime_list,2)))
products = np.prod(combos,axis=1)
unique_products = np.unique(products)
differences = unique_products[offset:] - unique_products[:-offset]
i=0
for difference in differences:
    if difference==1:
        print(differences[i], unique_products[i],unique_products[i+1])
        sys.exit()
    i+=1
