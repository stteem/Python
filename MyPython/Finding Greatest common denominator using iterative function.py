# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 01:16:06 2017

@author: Uwemuke
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    small = 0
    
    if a > b:
        small = b
    else:
        small = a
        
    while small > 0:
        if (a % small == 0) and (b % small == 0):
            print(small)
            break
        else:
            small -= 1
    return small
            
gcdIter(9, 12) 