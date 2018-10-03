# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 02:05:07 2017

@author: Uwemuke
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    out = 1
    for i in range(1, min(a, b)+1):
        if not a % i and not b % i:
            out = i
    return out