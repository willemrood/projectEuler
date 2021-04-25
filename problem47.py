from    functions import *
primes = []
for i in range(100):
    if isprime(i):
        primes.append(i)
primes = np.array(primes)
consec = 2
search = True
i = 1

valid_numbers = []
for start in range(10,100):
    number=start

    factors = number/primes
    valid_factors = factors[factors%1==0]
    numbers = number/valid_factors
    for i in numbers:
        factors = number / primes
        valid_factors = factors[factors % 1 == 0]
        if len(valid_factors)==0:
            print(start,i,j)

