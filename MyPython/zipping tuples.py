# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:37:02 2017

@author: Uwemuke
"""

a =[s, t]

s = "Toronto is the largest City in Canada"
t = "Python courses in Toronto by Bodenseo"
s = "".join(["".join(x) for x in zip(s,t)])

print(s)