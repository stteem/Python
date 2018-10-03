# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:38:13 2017

@author: Uwemuke
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    count = 0
    els = ()
    for i in L1:
        if i in L2:
            els[i] += 1
            count[i] +1
    else:
        return False
            
        
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']