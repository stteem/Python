# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:29:27 2017

@author: Uwemuke
"""
print("Please think of a number between 0 and 100!")
high = 100
low  = 0
guess = (high - low)//2.0

while guess**2 < high:

    print('Is your secret number' + str(guess) + '?')

     (input("Enter 'h' to indicate the guess is too high. \
             Enter 'l' to indicate the guess is too low.\
             Enter 'c' to indicate I guessed correctly.\
             :"  ))
if ans == 'h':
    high = guess
elif ans == 'l':
    low = guess
elif ans == 'c':
    print('Game over. Your secret number was: ' + str(guess))
else:
    print('Sorry, i did not understandd your input.')