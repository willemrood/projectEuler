number = 1
for i in range(1,101):
    number = number*i
sum=0
for i in str(number):
    sum+=int(i)
print(sum)