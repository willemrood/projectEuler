import numpy as np
threes = np.arange(0,1000,3)
fives = np.arange(0,1000,5)
fifteens = np.arange(0,1000,15)
total = sum(threes) + sum(fives) - sum(fifteens)
print(total)

