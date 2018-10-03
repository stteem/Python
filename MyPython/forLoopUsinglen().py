# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:12:12 2017

@author: Uwemuke
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))