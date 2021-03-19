def trianglenumber(n):
    return n*(n+1)/2
def pentagonalnumber(n):
    return n*(3*n-1)/2
def hexagonalnumber(n):
    return n*(2*n-1)
import numpy as np
numbers = []
for i in range(100000):
    numbers.append(trianglenumber(i))
    numbers.append(pentagonalnumber(i))
    numbers.append(hexagonalnumber(i))
numbers=np.array(numbers)
unique_numbers = np.unique(numbers)
for number in unique_numbers:
    args = np.where(numbers==number)[0]
    if len(args)>2:
        print(number,args)