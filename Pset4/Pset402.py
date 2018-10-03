# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 00:19:54 2017

@author: Uwemuke
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    update_hand = hand.copy()
    for i in word:
        update_hand[i] -= 1
    return update_hand
    
updateHand({'u': 1, 'a': 1, 'i': 1, 'l': 2, 'q': 1, 'm': 1}, 'quail')