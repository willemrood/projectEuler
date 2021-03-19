from itertools import permutations
i = 1
for perm in permutations([0,1,2,3,4,5,6,7,8,9]):
    if i==1e6:
        print(i,perm)
    i+=1