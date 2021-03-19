import numpy as np
from functions import *
lim=28123

abundants = []
for i in range(lim):
    if abundantNumber(i):
        abundants.append(i)
print(abundants)
print(len(abundants))
abundants=np.array(abundants)
all = []
for a in abundants:
    bs = abundants[abundants+a<lim]
    cs = bs+a
    for c in cs:
        all.append(c)
all = np.unique(all)
notall = []
for i in range(lim):
    if i not in all:
        notall.append(i)
print(notall)
print(np.array(notall).sum())