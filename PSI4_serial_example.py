# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:27:56 2023

@author: smith
"""

import psi4
import numpy as np
import time
import matplotlib.pyplot as plt

start=time.time()


#Ineffecient to read and write large data outside of scratch
psi4.set_output_file('output.dat', False)

geo_str="""
O
H 1 0.96
H 1 0.96 2 A"""

psi4.geometry(geo_str)
energies=[]
angles=np.linspace(80,120,num=320)
for a in angles:
    psi4.geometry(geo_str.replace("A",str(a)))
    psi4.set_options({'scf_type': 'df',
                      'freeze_core': True})
    energies.append(psi4.energy('scf/cc-pvdz'))

plt.scatter(angles,energies)
plt.savefig('serial.png')
minenergy=min(energies)
minangle=angles[energies.index(minenergy)]
print("Min energy found "+str(minenergy)+" at angle "+str(minangle))

end=time.time()
print("Elapsed Time",end-start)
