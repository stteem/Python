# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 15:24:34 2017

@author: Uwemuke
"""
HAND_SIZE = 7
n = HAND_SIZE
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
   
    SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    score = 0
    char_score = []
    if word == '':
        return 0
    else:
        for char in word:
            if char in SCRABBLE_LETTER_VALUES:
                char_score.append(SCRABBLE_LETTER_VALUES.get(char))
        score += sum(char_score) * len(word)
        if len(word) == n:
            score = score + 50
        else:                   
            print(score)
    return score
                    
getWordScore('babylon', n)     