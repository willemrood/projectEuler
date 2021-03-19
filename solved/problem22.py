def alp2num(letter):
    alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return alphabet.index(letter)+1

def name2sum(name):
    sum = 0
    for letter in name:
        sum+=alp2num(letter)
    return sum

with open('../data/p022_names.txt', 'r') as f:
    names = f.readlines()[0].split(sep=',')
i=0
for name in names:
    names[i] = name.strip('"')
    i+=1
names_sort = sorted(names)

nameValues = []
for i in range(len(names_sort)):
    nameValues.append((i+1)*name2sum(names_sort[i]))
print(sum(nameValues))



