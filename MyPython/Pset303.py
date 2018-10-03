# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 01:35:06 2017

@author: Uwemuke
"""


import string
def getAvailableLetters(*lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
        
    alphabets = [string.ascii_lowercase]
    print(alphabets.remove(*lettersGuessed))
    
    
getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])