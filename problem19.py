import numpy as np
days = np.arange(0,365*102)
days = days%7
nonleap = [31,28,31,30,31,30,31,31,30,31,30,31]
leap    = [31,29,31,30,31,30,31,31,30,31,30,31]
months = []
for i in range(101):
    if (1900+i)%4==0:
        #leapyear
        if (1900+i)%400==0:
            months.append(nonleap)
        else:
            months.append(leap)
    else:
        months.append(nonleap)
months = np.array(months)
count = 1
entry = 0
year = 1900
for i in range(101):
    for j in range(12):
        if year>=1901 and year<=2000 and days[entry]==6:
            count+=1
            print(year,j+1)
        entry+=months[i, j]
    year+=1
print(count)