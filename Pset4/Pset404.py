# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 17:56:41 2017

@author: Uwemuke
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length = sum(hand.values())
    return length
