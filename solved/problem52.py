import sys
import time
t0 = time.time()
from itertools import permutations
for i in range(100,1000000):
    i_str = str(i)
    count = 0
    for multiplier in range(2,7):
        new_i_str = str(i*multiplier)
        target = len(i_str)
        match=True
        for j in i_str:
            if j not in new_i_str:
                match = False
                break
        for j in new_i_str:
            if j not in i_str:
                match = False
                break
        if match:
            count+=1
    if count==5:
        print(i,i*2,i*3,i*4,i*5,i*6)
        print(time.time()-t0)
        sys.exit()