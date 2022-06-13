import sys

from functions import *
# replace part of number with the same digit
# the parts can be anywhere but the last
# check if prime

primes = []
for number in range(56003,int(56003+40e3)):
    if isprime(number):
        prime_string = str(number)
        # replace 1-x
        print(number)

        for numbers_to_replace in range(len(prime_string)-1):
            replace = []
            for positions_to_replace in range(len(prime_string)):
                replace.append(positions_to_replace)
            print(replace)
        sys.exit()


