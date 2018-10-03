# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:27:01 2017

@author: Uwemuke
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    animals = aDict
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result
    
how_many({ 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']})