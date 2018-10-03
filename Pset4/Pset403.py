# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:07:00 2017

@author: Uwemuke
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    isWord = True
    if word not in wordList:
        isWord = False
    wordDict = getFrequencyDict(word)
    for key in wordDict:
        try:
            if hand[key] - wordDict[key] < 0:
                isWord = False
        except KeyError:
            isWord = False
    return isWord
