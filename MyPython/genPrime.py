# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:12:19 2017

@author: Uwemuke
"""

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last