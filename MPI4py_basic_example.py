# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:25:44 2023

@author: smith
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
mpi_size = MPI.COMM_WORLD.Get_size()

if rank == 0:
    output=[]
    for i in range(mpi_size-1):
        data = comm.recv(source=MPI.ANY_SOURCE)
        output.append(str(rank)+" recieved:"+data)
    print(output)
else:
    msg="hello from "+str(rank)
    comm.send(msg, dest=0)
    
    