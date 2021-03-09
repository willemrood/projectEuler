from functions import *
sum=0
for i in range(int(1e6)):
    bin_string = bin(i)
    if ispalindrone(i) and ispalindrone(bin_string[2:]):
        sum+=i
print(sum)