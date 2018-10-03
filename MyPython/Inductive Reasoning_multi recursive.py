# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:30:35 2017

@author: Uwemuke
"""

def multi(a, b):
    
    if b == 1:
        return a
    
    else:
        
        return a + multi(a, b -1)
    