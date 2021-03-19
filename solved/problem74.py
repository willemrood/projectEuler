from functions import *
count = 0
for i in range(1000000):
    seq = factorialLoop(i)
    if len(seq)==60:
        print(i,seq)
        count+=1
print(count)