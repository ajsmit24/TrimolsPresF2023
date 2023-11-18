# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:20:24 2023

@author: smith
"""

import time
nums=list(range(int(5e7)))

def unbranched_find(n):
    found=-1
    for i in range(len(nums)):
        if(nums[i]==n):
            found=i
    return found

def branched_find(n):
    for i in range(len(nums)):
        if(nums[i]==n):
            return i
    return -1

unbranched_start=time.time()
unbranched_find(5)
unbranched_end=time.time()
print("unbranched time:",unbranched_end-unbranched_start)

branched_start=time.time()
branched_find(5)
branched_end=time.time()
print("branched time:",branched_end-branched_start)