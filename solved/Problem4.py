import itertools as it
import functions as func
import numpy as np





palindrones = []
digits = 3
for i in range(10**digits):
    for j in range(10**digits):
        product = i*j
        if func.ispalindrone(product):
            palindrones.append([i,j,product])
palindrones = np.array(palindrones)
print(max(palindrones[:,2]))
