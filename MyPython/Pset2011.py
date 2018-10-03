# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 03:08:47 2017

@author: Uwemuke
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
    
while month < 12:
    minPay = balance * monthlyPaymentRate
    unpaidBal = balance - minPay
    MonthlyInterest = unpaidBal * annualInterestRate/12.0 
    balance = unpaidBal + MonthlyInterest
    
    month += 1
        
print('Remaining balance is:', "%.2f" % balance)