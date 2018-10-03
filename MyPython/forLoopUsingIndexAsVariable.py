# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:21:15 2017

@author: Uwemuke
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))