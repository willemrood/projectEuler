import numpy as np
solutions=[]
for p in range(1,1001):
    print(p)
    sum=0
    for a in range(1,p-1):
        for b in range(1,p-a):
            c=(a**2+b**2)**0.5
            if a+b+c==p:
                sum+=0.5
    if sum>0:
        solutions.append([p,sum])
solutions=np.array(solutions)
print(solutions)