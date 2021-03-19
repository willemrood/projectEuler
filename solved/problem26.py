fractions = []
results = []
from decimal import *
getcontext().prec = 2000
for i in range(1,1000):
    frac = (Decimal(1)/Decimal(i)).to_eng_string()
    frac = frac[2:-1]
    frac = frac.lstrip('0')

    if len(frac)>10:
        j=1
        search=True
        while search:
            a = frac[:j]
            b = frac[j:j*2]
            c = a[:len(b)]
            if b==c:
                search=False
                if j>700 and j<1900:
                    print(i, j,b,c)
            j+=1

print(fractions)