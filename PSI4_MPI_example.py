# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:27:56 2023

@author: smith
"""

import psi4
import numpy as np
import time
import matplotlib.pyplot as plt

geo_str="""
O
H 1 0.96
H 1 0.96 2 A"""

def calc_energy(angle):
    psi4.set_output_file('output.dat', False)
    psi4.geometry(geo_str.replace("A",str(angle)))
    psi4.set_options({'scf_type': 'df',
                      'freeze_core': True})
    nrgy=psi4.energy('scf/cc-pvdz')    
    return nrgy

if __name__ == '__main__':
    start=time.time()
    energies=[]
    angles=np.linspace(80,120,num=320)
    from mpi4py.futures import MPIPoolExecutor
    with MPIPoolExecutor() as pool:
        energies = pool.map(calc_energy, angles)
    print("CALCULATIONS DONE")
    energies=[n for n in energies]
    plt.scatter(angles,energies)
    plt.savefig('MPI.png')
    minenergy=min(energies)
    minangle=angles[energies.index(minenergy)]
    print("Min energy found "+str(minenergy)+" at angle "+str(minangle))
    
    end=time.time()
    print("Elapsed Time",end-start)
