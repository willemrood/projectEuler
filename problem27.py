from functions import *
def somefunction(a,b):
    keep = True
    n = 0
    while keep:
        number = n**2+a*n+b
        if number>0:
            if isprime(number):
                n+=1
            else:
                keep = False
        else:
            keep = False
    return n

mem = 0
for a in np.arange(-999,1000):
    for b in np.arange(-1000,1001):
        seq = somefunction(a,b)
        if seq>mem:
            mem = seq
            print(a,b,seq,a*b)
