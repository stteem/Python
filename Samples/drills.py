# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 10:21:29 2017

@author: Uwemuke
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def get_Numer(self):
        return self.numer
    def get_Denom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.get_Denom() * self.get_Numer() \
                + other.get_Numer() * self.get_Denom()
        denomNew = other.get_Denom() * self.get_Denom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.get_Denom() * self.get_Numer() \
                    - other.get_Numer() * self.get_Denom()
        denomNew = other.get_Denom() * self.get_Denom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.get_Numer() / self.get_Denom()

oneHalf = fraction(1,2)
twoThirds = fraction(2,3)        