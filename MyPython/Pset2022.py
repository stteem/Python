# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:43:01 2017

@author: Uwemuke
"""
balance = 600
annualInterestRate = 0.2
temp = balance
minfixed = 0

while True:
    balance = temp
    for i in range(12):
        UnpaidBal = balance - minfixed
        MonthlyInterestRate = (annualInterestRate) / 12.0
        balance = UnpaidBal + (UnpaidBal * MonthlyInterestRate)
       
    if balance <= 0:
        print(round(minfixed))
        break
    
    else:
        minfixed += 10