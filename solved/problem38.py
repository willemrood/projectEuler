import numpy as np
for i in range(9,10000):
    for j in range(2,11):
        text = ''
        for k in range(1,j):
            text += str(i*k)
        if len(text)==9 and '0' not in text:
            numbers = []
            for t in text:
                numbers.append(int(t))
            if len(np.unique(numbers))==9:
                print(i,j-1,text)


