# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:34:35 2023

@author: smith
"""

import AndrewsHiddenThirdPartyLibrary as AHTPL
import time
start=time.time()

items=AHTPL.function1(500)
new_items=[AHTPL.function3(i) for i in items]

sq_items=[i*i for i in new_items]

end=time.time()
print("TIME ELAPSED:",end-start)