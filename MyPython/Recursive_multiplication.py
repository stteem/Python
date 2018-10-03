# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:21:17 2017

@author: Uwemuke
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(4))