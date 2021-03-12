from functions import *
from itertools import permutations
sum=1
all = [2,3,5,7]
for i in range(9,int(1e6),2):
    circular = False
    if "2" not in str(i) and "5" not in str(i) and "0" not in str(i):
        if i not in all:
            if isprime(i):
                primes = []
                for perm in permutations(str(i)):
                    number=""
                    for p in perm:
                       number+=p
                    if isprime(int(number)):
                        primes.append(int(number))
                    else:
                        break

                if len(primes)==factorial(len(str(i))):
                    circular=True
                    print(i, primes)
                    for prime in primes:
                        all.append(prime)
                    sum+=1
print(np.unique(all))
print(len(np.unique(all)))