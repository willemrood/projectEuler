#amicable pairs <3
import time
import numpy as np
t0=time.time()
def sumprop(n):
    sum=0
    for i in range(1,1+int(np.ceil(n/2))):
        if n%i==0:
            sum+=i

    return sum

def amicable(n1):
    isAmicable = False
    n2 = sumprop(n1)
    n3 = sumprop(n2)
    if n1==n3 and n1!=n2:
        isAmicable = True
        print(n1,n2,n3)
    return isAmicable
sum = 0
for i in range(1,10000):
    sum+=i*amicable(i)
print(sum)
t1=time.time()
print(t1-t0)