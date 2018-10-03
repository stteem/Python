# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 03:32:18 2017

@author: Uwemuke
"""
x = int(input('Enter an interger: '))
for guess in range(abs(x + 1)):
    if guess**3 >=abs(x):
        break
    if guess**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            guess -= guess
        print("Cube root of" + str(x) + "is" + str(guess))