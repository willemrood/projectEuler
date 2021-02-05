import numpy as np
#can be improved!!!!!!
numbers = np.arange(1,1000)
for a in numbers:
    for b in numbers:
        if b<a:
            continue
        for c in numbers:
            if c<b:
                continue
            if a+b+c==1000:
                if a**2+b**2==c**2:
                    print(a*b*c)


