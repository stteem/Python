# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:01:43 2017

@author: Uwemuke
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for all in secretWord:
        if secretWord not in lettersGuessed:
            return False
        else:
            True            

isWordGuessed('apple',['e', 'i', 'k', 'p', 'r', 's'])