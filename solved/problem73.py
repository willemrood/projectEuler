import numpy as np

start = 1/3
end= 0.5
limit = 12000
a = np.array(np.arange(1,limit+1)) * np.ones((1,limit))
b = np.array(np.arange(1,limit+1)) * np.ones((1,limit))
c  = a/b.T
d = np.unique(c)
e = d[d<0.5]
f = e[e>start]
print(len(f))