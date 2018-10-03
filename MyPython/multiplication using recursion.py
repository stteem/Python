# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:06:18 2017

@author: Uwemuke
"""

def recurPower(base, exp):
    
    if exp <= 0:
        return 1
    else:
        
        return base * recurPower(base, exp - 1)
        
print(recurPower(5, 5))