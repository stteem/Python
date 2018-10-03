# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 06:28:03 2017

@author: Uwemuke
"""

def build_shift_dict(self, *shift):
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
#    aDict = list(string.ascii_lowercase)
#    bDict = list(string.ascii_uppercase)
##    print(range(len(aDict)))   
#    for char in range(len(aDict)):
#        newDict = {}
#        newDict = 
#        print(newDict)
        
        
    aDict = dict(zip(string.ascii_lowercase, range(0, 26)))
    bDict = dict(zip(string.ascii_uppercase, range(0, 26)))
#    print(aDict)
    newDict = aDict.copy()
    for i in aDict:
        if i in newDict:
            newDict = aDict[i] + 2
            print(newDict)
#    print(newDict)
#    aDict = list(string.ascii_lowercase,string.ascii_uppercase)
#    print(adict)
#    print(aDict)
#    print(newDict)
#    for char in aDict:
#        aDict.values() = (aDict[char] + shift) % 26
#        print(aDict)
#    for char in bDict:
#        print(bDict)
#        bDict.values() = (bDict[char] + shift) % 26
        
#    shift = int(input("Enter your shift number between 0 and 26: "))
#    words = get_valid_words(self)
#    for i in aDict and bDict:
#        shifted.get(key[i])
#         shift = (aDict.values()[i] + shift_key) % 26
#         print(shifted.keys())
         
aDict = build_shift_dict(0)
#bDict = build_shift_dict(2)
#newDict = build_shift_dict(aDict, bDict)