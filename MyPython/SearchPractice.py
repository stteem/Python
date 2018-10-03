# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:28:59 2017

@author: Uwemuke
"""


high = 100
low  = 0
guess = (high - low)//2
x = guess
ans = 'h' or 'l' or 'c'

print("Please think of a number between 0 and 100!")

while (guess**2) > x:
    guess - low
    
    print('Is your secret number' +  str(guess)  + '?')
    
    print("Enter 'h' to indicate the guess is too high") 
    print("Enter 'l' to indicate the guess is too low")
    print("Enter 'c' to indicate I guessed correctly")
    
    
ans = print(input("Enter letter:"  ))

if ans == 'h':
    high = guess
elif ans == 'l':
    low = guess
elif ans == 'c':
    print('Game over. Your secret number was: ' + str(guess))
else:
    print('Sorry, i did not understandd your input.')