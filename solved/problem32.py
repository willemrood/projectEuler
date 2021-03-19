import numpy as np
from itertools import combinations,permutations
numbers = [1,2,3,4,5,6,7,8,9]
orders = []
for perm in permutations(numbers,9):
    number_str = ""
    for p in perm:
        number_str+=str(p)
    orders.append(number_str)
combs = []
for order in orders:
    for len_a in range(1,5):
        for len_b in range(1,9-len_a):
            len_c = 9-len_a-len_b
            a = int(order[:len_a])
            b = int(order[len_a:-len_c])
            c = int(order[-len_c:])

            if a*b==c:
                print(a,b,c)
                combs.append([a,b,c])
combs = np.array(combs)
print(np.sum(np.unique(combs[:,2])))