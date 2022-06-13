from functions import *
from itertools import combinations,permutations
primes=[]
for p in range(3,10000,2):
    if isprime(p):
        primes.append(p)
print("primes made: {}".format(len(primes)))
n=5
for set in combinations(primes,n):
    if 5 not in set:
        search =True
        for subset in combinations(set,2):
            a = str(subset[0])+str(subset[1])
            b = str(subset[1])+str(subset[0])
            if isprime(int(a)) and isprime(int(b)):
                pass
            else:
                search=False
                break
        if search:
            print(set)
            print(sum(set))
            break