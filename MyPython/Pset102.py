# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 14:28:49 2017

@author: Uwemuke
"""

s = 'azcbobobegghakl'
for char in range(3):
    if char == 'bob':
        char += 1
print('Number of times bob occurs is : ' + str(char))