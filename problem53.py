import sys
from itertools import combinations

for n in range(1,100):
    for r in range(1,n):
        ways = list(combinations(str(n),r))

        print(n,r,len(ways))
    if n ==5:
        sys.exit()