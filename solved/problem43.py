from itertools import permutations
numbers = [0,1,2,3,4,5,6,7,8,9]
totalsum=0
for perm in permutations(numbers,10):
    number=''
    for p in perm:
        number = number + str(p)
    check1 = int(number[1:4]) % 2 == 0
    if check1:
        check2 = int(number[2:5]) % 3 == 0
        if check2:
            check3 = int(number[3:6]) % 5 == 0
            if check3:
                check4 = int(number[4:7]) % 7 == 0
                if check4:
                    check5 = int(number[5:8]) % 11 == 0
                    if check5:
                        check6 = int(number[6:9]) % 13 == 0
                        if check6:
                            check7 = int(number[7:10]) % 17 == 0
                            if check7:
                                totalsum+=int(number)
                                print(number)
print(totalsum)
