import sys
import string
alphabet=list(string.ascii_uppercase)

import numpy as np
path = "/data/p042_words.txt"
with open("/data/p042_words.txt", 'r') as fh:
    for line in fh:
        words_list = line.split(sep=',')
triangle_numbers = []
for n in range(21):
    triangle_numbers.append(0.5*n*(n+1))

mem=0
for word in words_list:
    word_value = 0
    for letter in word[1:-1]:
        word_value+=1+alphabet.index(str(letter))
    if word_value in triangle_numbers:
        mem+=1
print(mem)


