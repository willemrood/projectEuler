import numpy as np
import time

def ispandigital(n):
    state=False
    if "0" not in (str(n)):
        digits = []
        for d in str(n):
            digits.append(int(d))
        if len(np.unique(digits))==len(str(n)) and np.max(digits)==len(str(n)):
            state=True
    return state

def romanvalue(stringofletters):
    romans = ['I','V','X','L','C','D','M']
    values = [1,5,10,50,100,500,1000]
    value=0
    for letter in stringofletters:
        value+=values[np.where(romans==letter)]
    return value

def isprime(x: int):
    run = True
    state = False
    if x == 2 or x == 3:
        run = False
        state = True
    if x%2 == 0 and run:
        run = False
        state = False
    if run:
        limit = np.sqrt(x)
        limit = int(np.ceil(limit))
        for i in np.arange(3,limit+1):
            if x%i==0:
                break
            if i == limit:
                state = True
    return state
def factorial(n):
    numbers = range(1,n+1)
    product=1
    for i in numbers:
        product=product*i
    return product

def ispalindrone(x):
    a = str(x)
    b = a[::-1]
    if a==b:
        state = True
    else:
        state = False
    return state

def properDivSum(n):
    divisors = np.arange(1,n//2+1)
    return np.sum(divisors*((n / divisors) % 1 == 0))

def abundantNumber(n):
    if properDivSum(n)>n: state=True
    else: state=False
    return state

def tictoc(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        functionname = str(func).split()
        print('Function '+functionname[1]+ ' took {} seconds'.format( time.time() - t0))
        return result
    return wrapper

def fibbo(n):
    sequence = []
    if type(n)==int:
        sequence =[1,1]
        for i in range(1,n-1):
            sequence.append( sequence[-2]+sequence[-1])
    if type(n) == list:
        sequence = n
        if len(sequence) >=2:
            sequence.append( sequence[-2]+sequence[-1])
    return sequence

def factorialDigits(n):
    sum=0
    for i in str(n):
        sum+=factorial(int(i))
    return sum

def factorialLoop(n):
    sequence = [n]
    loop = True
    while loop:
        n = factorialDigits(n)
        if n in sequence:
            loop = False
        else:
            sequence.append(n)
    return sequence