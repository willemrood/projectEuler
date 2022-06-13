def reverse(number):
    number_string= (str(number))
    string_number = ''
    for digit in number_string:
        string_number = digit + string_number
    return int(string_number)

def operation(number):
    number = number + reverse(number)
    return  number

from functions import *

count = 0
for test in range(0,10000):
    number = test
    for iterations in range(50-1):
        new_number = operation(number)
        if ispalindrone(new_number):
            print(test,new_number,1+iterations)
            count+=1
            break
        number = new_number
print(count)

