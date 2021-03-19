from functions import *
# import matplotlib.pyplot as plt
import numpy as np
path = "D:\Python\Projects\projectEuler\data\p079_keylog.txt"
logs = np.genfromtxt(path, delimiter=",").astype(int)
one = []
two = []
three = []
for log in logs:
    print(str(log))
    one.append(int(str(log)[0]))
    two.append(int(str(log)[1]))
    three.append(int(str(log)[2]))
print(one,two,three)

for i in range(10):
    if i not in one:
        print(1,i)
    if i not in two:
        print(2,i)
    if i not in three:
        print(3,i)