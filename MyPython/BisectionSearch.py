# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:40:08 2017

@author: Uwemuke
"""

x = 25
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))