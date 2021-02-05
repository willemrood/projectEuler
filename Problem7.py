import numpy as np
import scipy as sp
import pandas as pd
import functions as func
import matplotlib.pyplot as plt
primes = [2,3]
number = 3
while len(primes) < 10001:
    if func.isprime(number):
        primes.append(number)
    number+=2
print(primes[-1])