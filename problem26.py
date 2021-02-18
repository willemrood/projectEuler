fractions = []
results = []
for i in range(1,100):
    frac = str(1/i)
    frac = frac[2:]
    frac = frac.lstrip('0')
    fractions.append(frac)
    if len(frac)>15:
        print(frac)