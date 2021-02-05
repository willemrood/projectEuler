import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import random as rndm



Ncc = np.linspace(1,1e6,1000)
Adisk = np.pi*40000**2
Vdisk = Adisk*2000
Asquare = 2000**2
Acircle = np.pi * 1000**2
Vcube = 2000**3
Vsphere = 4/3 * np.pi *1000**3

print(Adisk/Asquare)
print(Adisk/Acircle)
print(Vdisk/Vcube)
print(Vdisk/Vsphere)

D1 = 2*(3*Vdisk/4/np.pi/Ncc)**(1/3)
D2 = 2*(Adisk/np.pi/Ncc)**(0.5)

plt.figure(1)
plt.loglog(Ncc,D1, label = 'Volume')
plt.loglog(Ncc,D2, label = 'Area')
plt.grid(True, which="both")
plt.xlabel('Ncc [-]')
plt.ylabel('Distance [Light years]')
plt.legend()
plt.show()



