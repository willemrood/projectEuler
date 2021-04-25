import matplotlib.pyplot as plt

from functions import *
# import matplotlib.pyplot as plt
import numpy as np
path = "D:\Python\Projects\projectEuler\data\p079_keylog.txt"
logs = np.genfromtxt(path, delimiter=",").astype(int)
one = []
two = []
three = []
all = []
for log in logs:
    print(str(log))
    one.append(int(str(log)[0]))
    two.append(int(str(log)[1]))
    three.append(int(str(log)[2]))
    all.append(int(str(log)[0]))
    all.append(int(str(log)[1]))
    all.append(int(str(log)[2]))

import numpy as np
all = np.array(all)
digits = np.unique(all)
print(digits)


for i in digits:
    if i not in one:
        print("not in first entries:",i)
    if i not in two:
        print("not in second entries:",i)
    if i not in three:
        print("not in third entries:",i)


fig,((ax1),(ax2),(ax3)) = plt.subplots(1,3)
ax1.hist(one,bins=[0, 1,2,3,4,5,6,7,8,9])
ax2.hist(two,bins=[0, 1,2,3,4,5,6,7,8,9])
ax3.hist(three,bins=[0, 1,2,3,4,5,6,7,8,9])
plt.show()