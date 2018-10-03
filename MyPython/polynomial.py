# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 06:20:50 2017

@author: Uwemuke
"""

def general_poly (L):
    def evaluate(L, x):
        k = 0
        ans = 0
        for number in reversed(L):
            ans += number * x ** k   
            k += 1
        return ans
general_poly([1, 2, 3, 4])(10)