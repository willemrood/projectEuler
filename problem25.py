from functions import *

@tictoc
def fibboLength(n):
    while len(str(n[-1])) < 1000:
        n= fibbo(n)
    print(len(n), len(str(n[-1])), n[-1])
    return

sequence = [1,1]
fibboLength(sequence)