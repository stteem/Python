# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 03:00:16 2017

@author: Uwemuke
"""

s = 'azcbobobegghakl'
longest = curr = s[0]
for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        curr += s[i]
    else: curr = s[i]
    if len(curr) > len(longest):
        longest = curr
print('Longest substring in alphabetical order is: ', longest)