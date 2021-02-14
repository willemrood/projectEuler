from functions import *
from itertools import combinations
import matplotlib.pyplot as plt
abundants = []
values = []
for i in range(1,28123):
    sum = properSum(i)
    if i<sum:
        abundants.append(i)
        values.append(sum)
combos = []
for i in combinations(abundants,2):
    if i[0]+i[1]<28123:
        combos.append([i[0]+i[1]])
print(combos)

