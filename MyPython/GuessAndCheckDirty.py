# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 04:04:16 2017

@author: Uwemuke
"""

x = int(input('Enter an interger: '))
ans = 0 
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))