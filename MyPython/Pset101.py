# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 12:44:02 2017

@author: Uwemuke
"""

s = 'azcbobobegghakl'
count = 0 
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print('Number of vowels : ' + str(count))