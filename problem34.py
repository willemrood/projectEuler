from functions import *
from itertools import combinations,permutations
factorials = []
numbers = [0,1,2,3,4,5,6,7,8,9]
for n in numbers:
    factorials.append(factorial(n))
print(factorials)
totalsum=0
for i in range(3,int(1e9)):
    sum = 0
    for digit in str(i):
        sum+=factorials[int(digit)]
    if i==sum:
        totalsum+=i
        print(i,totalsum)
