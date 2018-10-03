# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 06:28:03 2017

@author: Uwemuke
"""

def build_shift_dict(self, shift):
    import string

    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
#    self.shifted = {}
    aDict = dict(zip(string.ascii_lowercase, range(0, 26)))
    bDict = dict(zip(string.ascii_uppercase, range(0, 26)))
    print(aDict)
    shift = int(input("Enter your shift number between 0 and 26: "))
    words = 'mother'
    for i in words:
        if i in aDict:
         shift = (aDict.values()[i] + shift_key) % 26
         print(shifted.keys())
         
#get_valid_words('mother')        
