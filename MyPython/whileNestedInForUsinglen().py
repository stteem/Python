# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:05:18 2017

@author: Uwemuke
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))