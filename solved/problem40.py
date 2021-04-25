import numpy as np
number='0.'
digit_count = 2
i=1
while digit_count<1000010:
    number=number+str(i)
    digit_count+=len(str(i))
    i+=1
print(digit_count)
print(number[2],number[3],number[4])
result = 1

for index in np.logspace(1,6,6)+1:
    print(int(index))
    result = result * int(number[int(index)])
print(result)