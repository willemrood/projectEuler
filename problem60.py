from functions import *
from itertools import combinations,permutations
primes=[]
for p in range(1,200,2):
    if isprime(p):
        primes.append(p)
n=5
for set in combinations(primes,n):
    if 5 not in set:
        count=0
        i = 0
        for subset in combinations(set,2):
            i+=1
            a = str(subset[0])+str(subset[1])
            b = str(subset[1])+str(subset[0])
            if isprime(int(a)) and isprime(int(b)):
                count+=1

        if count==10:
            print(set,i,count)