# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 01:47:40 2017

@author: Uwemuke
"""

cube = -8
for guess in range(abs(cube) +1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))