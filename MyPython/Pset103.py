# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:48:08 2017

@author: Uwemuke
"""

s = 'azcbobobegghakl'
longest = s[0]
temp = s[0]
for i in range(1,len(s)):
    if s[i] >= temp[-1]:
        temp += s[i]
        if len(temp) > len(longest):
            longest = temp
    else:
        temp = s[i]
print("Longest substring in alphabetical order is: %s" % (longest))
        