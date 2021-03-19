def pentagonnumber(n):
    return n*(3*n-1)/2
import numpy as np
pentagonals=[]

for i in range(1000,2500):
    pentagonals.append(pentagonnumber(i))
pentagonals = np.array(pentagonals)
for i in pentagonals:
    larger = pentagonals[pentagonals>i]
    for j in larger:
        sum = i+j
        diff = j-i
        if sum in pentagonals and diff in pentagonals:
            print(i,j,sum,diff)