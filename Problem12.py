
import math
t = 0
add = 1
fac = []
limit = int(input("Divisors needed: "))
while len(fac) < limit:
    t += add
    d = 1 #divisor
    fac = []
    print(t)
    while d < math.sqrt(t):
        if t % d == 0:
            fac.append(d)
            fac.append(t // d)
        d += 1
    add += 1

fac.sort()

print("Number: ", t)
print("divisors: ", len(fac))
print(fac)
