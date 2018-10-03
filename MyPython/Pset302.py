# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:35:55 2017

@author: Uwemuke
"""

def getGuessedWord(secretWord, lettersGuessed):
    word = []
    dash = ' _ '
    for i in secretWord:
        if i in lettersGuessed:
            word.append( i )
        else:
            word.append(dash) 
            
    return ''.join(word)
    
getGuessedWord('apple',['e', 'i', 'k', 'p', 'r', 's'])