# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:24:05 2017

@author: Uwemuke
"""

def oddTuples(*aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to 
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

aTup = oddTuples('I', 'am', 'a', 'test', 'tuple')