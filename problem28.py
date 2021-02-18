import numpy as np
size = 1001
spiralList = np.arange(1,1+size**2) #list that creates all the numbers inside the matrix
# the gaps between the numbers on the diagonals are fixed depending on the size
# it starts with 4*1, then 4*3, then 4*5 .... etc
# so you only need to sum those up
diagonalOffsets = []
for odds in np.arange(1,size,2):
    for i in range(4):
        diagonalOffsets.append(odds+1)
index = 0
sum = 0
for j in diagonalOffsets:
    sum += spiralList[index]
    index+=j
sum+= spiralList[index]
print(sum)