# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:58:35 2023

@author: smith
"""
import time

#not memoized
def not_memo_power_up_to_n(n):
    res=[]
    for i in range(n):
        p=i**i
        res.append(p)
    return res

#memoized
computed={}
def memo_power_up_to_n(n):
    res=[]
    for i in range(n):
        if(not i in computed):
            p=i**i
            res.append(p)
            computed[i]=p
        else:
            res.append(computed[i])
    return res

not_mem_start=time.time()
not_memo_power_up_to_n(500)
not_memo_power_up_to_n(1000)
not_memo_power_up_to_n(5000)
not_memo_power_up_to_n(7500)
not_memo_power_up_to_n(9000)
not_memo_power_up_to_n(10000)
not_mem_end=time.time()
print("Not memoized time:",not_mem_end-not_mem_start)

mem_start=time.time()
memo_power_up_to_n(500)
memo_power_up_to_n(1000)
memo_power_up_to_n(5000)
memo_power_up_to_n(7500)
memo_power_up_to_n(9000)
memo_power_up_to_n(10000)
mem_end=time.time()
print("Memoized time:",mem_end-mem_start)
