# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:58:11 2017

@author: Uwemuke
"""

def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

multi_iter(4, 8)