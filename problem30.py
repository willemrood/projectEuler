import numpy as np
from itertools import combinations,permutations
numbers = np.arange(10)
numbers_pow = numbers**5
print(numbers_pow)
summ=0
for i in numbers:
    for j in numbers:
        for k in numbers:
            for g in numbers:
                for h in numbers:
                    for f in numbers:
                        number = int(str(i)+str(j)+str(k)+str(g)+str(h)+str(f))
                        sum_pow = numbers_pow[i]+numbers_pow[j]+numbers_pow[k]+numbers_pow[g]+numbers_pow[h]+numbers_pow[f]
                        if number == sum_pow and number>1:
                            summ+=number
                            print(number)

print(summ)