import numpy as np

fib = [1, 2]
print(fib)
fibeven = []
while fib[-1] < 4e6:
    fib.append(fib[-1]+fib[-2])
print(fib[-1])

for i in range(fib.__len__()):
    if fib[i]%2 ==0:
        fibeven.append(fib[i])
print(fibeven)
print(sum(fibeven))