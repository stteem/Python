# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 02:31:40 2017

@author: Uwemuke
"""

def fib(x):
    '''assumes x  an int >= 0
        returns Fibonacci of x'''
    
        if x == 0 or x == 1:
            return 1
        else:
            return fib(x-1) + fib(x-2)