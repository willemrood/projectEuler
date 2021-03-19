import numpy as np
import itertools as itt

data = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80 ,70, 33],
[41, 48, 72, 33, 47, 32, 37, 16 ,94 ,29],
[53, 71, 44, 65, 25, 43, 91, 52 ,97, 51 ,14],
[70, 11, 33, 28, 77, 73, 17, 78 ,39, 68, 17 ,57],
[91, 71, 52, 38, 17, 14, 91, 43 ,58 ,50 ,27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38,53, 60, 4, 23]]
choices = 14
combos = 2**choices
best = 0

for i in range(combos):
    bin_string = bin(i)[2:]
    for zero in range(choices-len(bin_string)):
        bin_string = "0" + bin_string
    sum = 75
    index_mem = 0
    row_mem = 1
    history = []
    for j in bin_string:
        sum += data[row_mem][index_mem+int(j)]
        history.append(data[row_mem][index_mem+int(j)])
        index_mem += int(j)
        row_mem += 1
    if sum>best:
        best=sum
        best_history = history
print(best_history)
print(best)
