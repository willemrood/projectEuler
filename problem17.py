import numpy as np
singles = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen']
tens = ['teen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
digits = ['','one','two','three','four','five','six','seven','eight','nine']


def numberLength(number):
    length=0
    numberString = str(number)
    stringOfNumber = ''
    if len(numberString) == 1:
        stringOfNumber += singles[number]
    if len(numberString)==2:
        try:
            #see if its twelve eleven..
            stringOfNumber +=singles[number]
        except:
            #if not decompose in first and second digit
            stringOfNumber +=tens[(number//10)-1]
            stringOfNumber +=digits[number%10]
    if len(numberString) == 3:
        stringOfNumber += digits[number//100] + 'hundred'
        if number%100 !=0:
            stringOfNumber+='and'
            try:
                # see if its twelve eleven..
                stringOfNumber += singles[number%100]
            except:
                # if not decompose in first and second digit
                stringOfNumber += tens[(number%100)//10 - 1]
                stringOfNumber += digits[(number%100)%10]
    if len(numberString) == 4:
        stringOfNumber = 'one thousand'
    print(number,stringOfNumber,len(stringOfNumber))
    return len(stringOfNumber)

sum=0
for j in range(10):

for i in range(1,100):
    sum+=numberLength(i)
print(sum)