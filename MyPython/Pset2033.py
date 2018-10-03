# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:49:49 2017

@author: Uwemuke
"""

balance = 320000
epsilon = 0.01
annualInterestRate = 0.2
upper =  balance + (balance * MonthlyInterestRate) / 12.0
lower = balance / 12
ans = (upper + lower)/2
x = upper
temp = balance

while (ans**2 - x) >= epsilon:
    balance = temp
    for i in range(12):
        MonthlyInterestRate = (annualInterestRate) / 12.0
        ans = balance + (balance * MonthlyInterestRate)/ 12
            
        if ans**2 < x:
            lower = ans
        else:
            upper = ans
            ans = (upper + lower)/2.0
            break

print("Lowest Payment:", "%.2f" % ans)
       
       