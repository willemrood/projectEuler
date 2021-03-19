import numpy as np
import scipy as sp
import pandas as pd

import matplotlib.pyplot as plt

x = np.arange(1,101)
sumofsquares = sum(np.power(x,2))
squaresofsum = sum(x)**2
print(sumofsquares)
print(squaresofsum)
print(squaresofsum-sumofsquares)