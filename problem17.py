import numpy as np
singles = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen']
tens = ['teen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']



def numberLength(number):
    length=0
    numberString = str(number)
    print(numberString)
    if len(numberString) == 1:
        length = len(singles[number])
    if len(str(number))==2:
        try:
            length = len(singles[number])
        except:
            print(tens[int(numberString[0])-1])
            print(singles[int(numberString[1])-1])
            length+= len(tens[int(numberString[0])-1])
            length+= len(singles[int(numberString[1])-1])
    return length


print(numberLength(40))
