# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 00:26:37 2017

@author: Uwemuke
"""
   
def dict_invert(d): 
    dkeys = list(d.keys())
    dvals = list(d.values())
    dzip = list(zip(dvals, dkeys))
    inverted = dict(dzip)
    print(inverted)
   
dict_invert({1:10, 2:20, 3:30})