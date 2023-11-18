# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:05:31 2023

@author: smith
"""
import json

class Logger():
    def __init__(self, filename):
        self.logfilename=filename
        f=open(filename,"w+")
        f.close()
    def log(self,s):
        f=open(self.logfilename,"a")
        f.write(json.dumps(s)+"\n")
        f.close()
        

mylogger=Logger("example.log")
mylogger.log("hellow world")
mylogger.log([{"A":2},3])