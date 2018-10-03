# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 03:26:56 2017

@author: Uwemuke
"""

import string
def getAvailableLetters(*lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    Guessedletters = ''.join(*lettersGuessed)   
    alphabets = set(string.ascii_lowercase)
    Guessed = set(Guessedletters)
    result = alphabets.difference(Guessed)
    ordered = sorted(result)
    
    return (''.join(ordered))
    
    
getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])