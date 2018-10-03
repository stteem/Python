# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:27:04 2017

@author: Uwemuke
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 