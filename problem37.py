from functions import *
i=10
count = 0
sum = 0
while count < 11:
    if isprime(i):
        if "2" not in str(i):
            left = True
            right = True
            leftnum = str(i)
            rightnum = str(i)
            while left and len(leftnum)>1:
                leftnum = leftnum[:-1]
                if not isprime(int(leftnum)):
                    left = False
            while right and len(rightnum)>1:
                rightnum = rightnum[1:]
                if not isprime(int(rightnum)):
                    right = False
            if left and right:

                count+=1
                sum+=i
                print(i,count,sum)
    i+=2