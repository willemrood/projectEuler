from itertools import permutations
from functions import *
solutions = []
for i in [5,6,7,8,9]:
    numbers = np.arange(1,i+1)
    for perm in permutations(numbers,i):
        number = ''
        for p in perm:
            number+=str(p)
        if isprime(int(number)):
            last = int(number)
print(last)