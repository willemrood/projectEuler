import numpy as np
limit = 100
sequence = []
for a in np.arange(2,limit+1):
    for b in np.arange(2,limit+1):
        sequence.append(a**b)
sequence = np.array(sequence)
sequence = np.sort(sequence)
sequence = np.unique(sequence)
print(sequence)
print(len(sequence))

