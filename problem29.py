import numpy as np
limit = 100
sequence = np.zeros((limit-1,limit-1))
for a in np.arange(2,limit+1):
    for b in np.arange(2,limit+1):
        sequence[a-2,b-2] = a**b

